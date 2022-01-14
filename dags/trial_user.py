from datetime import datetime, timedelta
from airflow import DAG
from custom import MySqlToPostgreOperator

dag = DAG(
    dag_id="a_job_near_rt",
    start_date=datetime.now() - timedelta(hours=1),
    schedule_interval="* * * * *",
    concurrency=100,
)

start = MySqlToPostgreOperator(
    task_id=f"start",
    sql="select * from user "
    "where created_at BETWEEN '{start_date}' "
    "AND '{end_date}'",
    target_table="public.user",
    identifier="id",
    dag=dag,
)
