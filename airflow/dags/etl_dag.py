from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 11, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'depends_on_past': False
}

with DAG(
    'etl_dag',
    default_args=default_args,
    catchup=False,
    description='This DAG triggers the PySpark ETL for the California Housing dataset',
    schedule_interval='@daily'
) as dag:

    start = EmptyOperator(task_id="Start")

    run_etl_categorical = BashOperator(
        task_id='ETL_Categorical_Columns',
        bash_command='python3 /opt/airflow/etl/etl_categorical.py',
        retries=1
    )

    run_etl_aggregation = BashOperator(
        task_id='ETL_Aggregation',
        bash_command='python3 /opt/airflow/etl/etl_aggregation.py',
        retries=1
    )

    end = EmptyOperator(task_id="End")

    start >> run_etl_categorical >> run_etl_aggregation >> end
