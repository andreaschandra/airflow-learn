from datetime import datetime
import airflow.utils.dates
from airflow import DAG
from airflow.operators.dummy import DummyOperator

dag = DAG(
    dag_id="listing_6_03_v4",
    start_date=datetime(2022, 1, 1),
    schedule_interval="@daily",
    concurrency=1,
    tags=["chapter6"]
)

create_metrics = DummyOperator(task_id="create_metrics", dag=dag)

for supermarket_id in [1, 2, 3, 4]:
    copy = DummyOperator(task_id=f"copy_to_raw_supermarket_{supermarket_id}", dag=dag)
    process = DummyOperator(task_id=f"process_supermarket_{supermarket_id}", dag=dag)
    copy >> process >> create_metrics