import time
from airflow import DAG
from datetime import datetime, timedelta, timezone
from airflow.operators.python import PythonOperator

default_args = {
  'owner': 'victor',
  'retries': 5,
  'retry_delay': timedelta(seconds=30)
}

def greet():
  print("hello... nevermind.")

def mymain():
    x = 0
    while True:
        x += 1
        print("version4: {}".format(x))
        time.sleep(1)

with DAG (
  dag_id = 'test_pythonop',
  default_args = default_args,
  description = 'This is test DAG',
  start_date = datetime(2024, 3, 1, 1, tzinfo=timezone.utc),
  schedule_interval = '@daily',
  catchup = False
) as dag:
    task1 = PythonOperator(
      task_id = 'mymain',
      python_callable = mymain
    )
    
    task1
    
