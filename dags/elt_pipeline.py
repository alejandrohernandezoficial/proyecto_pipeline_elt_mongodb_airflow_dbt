from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

from scripts.mongo_to_postgres import load_to_postgres

with DAG(
    dag_id="modern_elt_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    extract_load = PythonOperator(
        task_id="mongo_to_postgres",
        python_callable=load_to_postgres
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/dbt && dbt run"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/dbt && dbt test"
    )

    extract_load >> dbt_run >> dbt_test