from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
  'owner': 'victor',
  'retries': 2,
  'retry_delay': timedelta(minutes=5)
}

with DAG (
  dag_id = 'dag1',
  default_args = default_args,
  description = 'This is test DAG',
  start_date = datetime(2024, 3, 1, 1),
  schedule_interval = '@daily'
  
) as dag:
    task1 = BashOperator(
      task_id = 'task1',
      bash_command = 'echo "testing dags"'
    )
    
    task1
    
