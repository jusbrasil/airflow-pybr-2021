from datetime import datetime
from random import randint

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


def movie_chooser():
    with open("csvs/movies.csv") as movies_csv:
        movies = movies_csv.readlines()
        index = randint(0, len(movies) - 1)
        print(movies[index])
        return movies[index]


with DAG(
    "first_dag",
    start_date=datetime(2021, 10, 11),
    catchup=False,
) as dag:
    start = DummyOperator(task_id="start", dag=dag)
    # movie_choosen_1 = PythonOperator(
    #     task_id="choose_movie", callable=movie_chooser, dag=dag
    # )
    # movie_choosen_2 = PythonOperator(
    #     task_id="choose_movie_2", callable=movie_chooser, dag=dag
    # )

    # movie_choosen_3 = PythonOperator(
    #     task_id="choose_movie_3", callable=movie_chooser, dag=dag
    # )

    tasks = []
    for i in range(3):
        task = PythonOperator(
            task_id=f"choose_movie_{i}", callable=movie_chooser, dag=dag
        )
    end = DummyOperator(task_id="end", dag=dag)

    # start >> [movie_choosen_1, movie_choosen_2, movie_choosen_3] >> end
    start >> tasks >> end
