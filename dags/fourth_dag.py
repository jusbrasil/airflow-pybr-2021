from datetime import datetime
from random import randint

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


def movie_chooser(type, **context):
    with open("csvs/movies.csv") as movies_csv:
        movies = movies_csv.readlines()
        index = randint(0, len(movies) - 1)
        context["ti"].xcom_push(key=f"movie_choosed_{type}", value=movies[index])
        return movies[index]


# SENSOR esperando a outra dag escolher os filmes pra pegar eles do xcom

with DAG(
    "fourth_dag",
    start_date=datetime(2021, 10, 11),
    tags=["pybr-tutorial"],
    catchup=False,
) as dag:
    start = DummyOperator(task_id="start", dag=dag)
    tasks = []
    for i in range(3):
        task = PythonOperator(
            task_id=f"choose_movie_{i}",
            python_callable=movie_chooser,
            op_kwargs={"type": i},
            dag=dag,
            provide_context=True,
        )
    end = DummyOperator(task_id="end", dag=dag)
    start >> tasks >> end
