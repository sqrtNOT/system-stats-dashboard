from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
	'Temps',
	default_args={
		'depends_on_past': False,
		'retries': 0,
	},
	description='Parse the sensors command and store it in mysql',
	schedule_interval='* * * * *', #every minute
	start_date=datetime(2022, 6, 4),
	catchup=False,
) as dag:
	get_temps = BashOperator(
		task_id='get_temps',
		bash_command="sensors.sh ",
)


get_temps
