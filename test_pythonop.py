from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
  'owner': 'victor',
  'retries': 1
}

def greet():
  print("hello... nevermind.")

with DAG (
  dag_id = 'test_pythonop',
  default_args = default_args,
  description = 'This is test DAG',
  start_date = datetime(2024, 3, 1, 1),
  schedule_interval = '@daily',
  catchup = False
) as dag:
    task1 = PythonOperator(
      task_id = 'greet',
      python_callable = greet
    )
    
    task1
    