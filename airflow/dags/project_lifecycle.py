from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task, dag
from datetime  import datetime,timedelta
import os
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

@dag(
    dag_id='DataCamp',
    start_date=datetime.now(),
    schedule_interval=timedelta(hours=1),
)
def project_lifecycle():
    @task(task_id="test_airflow")
    def test_airflow():
        print("Hello Airflow")
        return "Hello Airflow"
    @task(task_id='ingest')
    def connect_snowFlake():
        logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
        account=os.getenv("SNOWFLAKE_ACCOUNT")
        user=os.getenv("SNOWFLAKE_USER")
        password=os.getenv("SNOWFLAKE_PASSWORD")
        database=os.getenv("SNOWFLAKE_DATABASE")
        schema=os.getenv("SNOWFLAKE_SCHEMA")
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE")

    @task(task_id='store_on_snowflake')
    def store_on_snowflake():


     test_airflow() >> connect_snowFlake()



dag=project_lifecycle()