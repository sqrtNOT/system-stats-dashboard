from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
	'Uptimer',
	default_args={
		'depends_on_past': False,
		'retries': 0,
	},
	description='Parse the uptime command and store it in mysql',
	schedule_interval='0 * * * *', #every hour
	start_date=datetime(2022, 6, 4),
	catchup=False,
) as dag:
	get_uptime = BashOperator(
		task_id='get_uptime',
		bash_command="uptime.sh ",
)


get_uptime
