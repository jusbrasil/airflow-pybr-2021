from datetime import datetime
from random import randint

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


def movie_chooser():
    with open("./dags/fixtures/movies.csv") as movies_csv:
        movies = movies_csv.readlines()
        index = randint(0, len(movies) - 1)
        print(movies[index])
        return movies[index]


with DAG(
    "first_dag",
    tags=["pybr-tutorial"],
    start_date=datetime(2021, 10, 11),
    catchup=False,
) as dag:
    start = DummyOperator(task_id="start", dag=dag)
    movie_choosen = PythonOperator(
        task_id="choose_movie", python_callable=movie_chooser, dag=dag
    )
    end = DummyOperator(task_id="end", dag=dag)

    start >> movie_choosen >> end
