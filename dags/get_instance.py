from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="get_instance_v6",
    start_date=datetime.today() - timedelta(minutes=60),
    schedule_interval="*/5 * * * *",
)

get_hostname = BashOperator(
    task_id=f"echo_hostname",
    bash_command=("hostname"),
    dag=dag,
)

for i in range(10):

    get_ip = BashOperator(
        task_id=f"get_ip_{i}",
        bash_command=("dig +short myip.opendns.com @resolver1.opendns.com"),
        dag=dag,
    )

    sleep = BashOperator(task_id=f"sleep_{i}", bash_command=("sleep 2"), dag=dag)

    get_hostname >> get_ip >> sleep
