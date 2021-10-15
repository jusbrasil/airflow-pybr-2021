from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor


def get_gross_year(type, **context):
    task_instance = context["ti"]
    movie_data_str = task_instance.xcom_pull(key=f"movie_choosed_{i}")
    movie_data = movie_data_str.split(",")
    return movie_data[-2:]


# SENSOR esperando a outra dag escolher os filmes pra pegar eles do xcom

with DAG(
    "fourth_dag",
    start_date=datetime(2021, 10, 11),
    tags=["pybr-tutorial"],
    schedule_interval="*/1 * * * *",
    catchup=False,
) as dag:
    start = DummyOperator(task_id="start", dag=dag)
    wait_movie_choose = ExternalTaskSensor(
        task_id="wait_movie_to_be_choosen",
        external_dag_id="movie_chooser_dag",
        external_task_id="end",
        execution_date_fn=lambda dt: dt + timedelta(minutes=10),
    )
    tasks = []
    for i in range(3):
        task = PythonOperator(
            task_id=f"get_gross_year_{i}",
            python_callable=get_gross_year,
            op_kwargs={"type": i},
            dag=dag,
            provide_context=True,
        )
        tasks.append(task)
    end = DummyOperator(task_id="end", dag=dag)
    start >> wait_movie_choose >> tasks >> end
