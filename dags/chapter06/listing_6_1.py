import airflow.utils.dates
from airflow import DAG
from airflow.sensors.filesystem import FileSensor

dag = DAG(
    dag_id="listing_6_01",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="0 7 * * *",
    description="A batch workflow for ingesting supermarket promotions data, demonstrating the FileSensor.",
    default_args={"depends_on_past": True},
    tags=["chapter6"]
)

wait = FileSensor(
    task_id="wait_for_supermarket_1", 
    filepath="/home/andreas/data/supermarket1/data.csv",
    dag=dag
)
