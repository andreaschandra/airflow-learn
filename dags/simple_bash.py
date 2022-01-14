import json
import pathlib

import airflow
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="simple_bash",
    start_date=airflow.utils.dates.days_ago(14),
    schedule_interval="@daily",
)

hello = BashOperator(
    task_id="hello",
    bash_command="echo Hello World",
    dag=dag,
)

hello