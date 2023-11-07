from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,  # Prevent catching up on missed runs
}

dag = DAG(
    'etl_dag',
    default_args=default_args,
    description='This DAG triggers the PySpark ETL for the California Housing dataset',
    schedule_interval='@daily'
)

run_etl = BashOperator(
    task_id='run_etl',
    bash_command='python3 /opt/airflow/etl/etl.py',
    retries=1,
    dag=dag
)
