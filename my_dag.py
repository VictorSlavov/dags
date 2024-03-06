from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
  'owner': 'victor',
  'retries': 2,
  'retry_delay': timedelta(minutes=5)
}

with DAG (
  dag_id = 'my_dag',
  default_args = default_args,
  description = 'This is test DAG',
  start_date = datetime(2024, 3, 1, 1),
  schedule_interval = '@daily',
  catchup = False
) as dag:
    task1 = BashOperator(
      task_id = 'my_dag_task1',
      bash_command = """
        set -e
        pwd
        ps
        echo $(date)
        pip list
        echo "Find me in the log"
      """
    )
    
    task1
    