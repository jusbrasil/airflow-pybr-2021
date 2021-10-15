from datetime import datetime

from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.dummy import DummyOperator

# mudando pra docker imagem pra usar o pandas e filtrar melhor o filme
with DAG(
    "fifth_dag",
    start_date=datetime(2021, 10, 11),
    tags=["pybr-tutorial"],
    catchup=False,
) as dag:
    start = DummyOperator(task_id="start", dag=dag)
    tasks = []
    genres = ["Romance", "Comedy", "Drama", "Animation", "Fantasy"]
    for genre in genres:
        task = DockerOperator(
            task_id=f"choose_movie_{genre}",
            dag=dag,
            image="pybr-tutorial",
            command=["python", "movie_chooser.py", genre],
            auto_remove=True,
        )
        tasks.append(task)
    end = DummyOperator(task_id="end", dag=dag)
    start >> tasks >> end
