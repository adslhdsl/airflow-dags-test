"""GitHub <-> Airflow Git DAG Bundle 연동 테스트용 DAG."""

import pendulum
from airflow.sdk import dag, task

VERSION = "v4"


@dag(
    dag_id="hello_github",
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["github-sync-test"],
)
def hello_github():
    @task()
    def say_hello() -> str:
        message = f"Hello from GitHub! ({VERSION})"
        print(message)
        return message

    @task()
    def show(message: str) -> None:
        print(f"received: {message}")

    @task()
    def report(message: str) -> None:
        print(f"[report] dag=hello_github version={VERSION} payload={message}")

    @task()
    def footer() -> None:
        print("-- end of dag --")

    msg = say_hello()
    show(msg)
    report(msg)
    footer()


hello_github()
