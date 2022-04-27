from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow import DAG

from github.includes.analysis import record_analysis
from github.includes.analysis import table_analysis
from github.includes.analysis import extract_database

default_args = {'owner': 'airflow', 'start_date': datetime(2021, 1, 1),'email': ['dummysource@gmail.com'],'email_on_failure': True}

dag = DAG('demoautomation', schedule_interval='@daily', default_args=default_args, catchup=False)

with dag:
    
    t1 = PythonOperator(task_id='t1',python_callable=record_analysis)
    t2 = PythonOperator(task_id='t2',python_callable=table_analysis)
    t3 = PythonOperator(task_id='t3',python_callable=extract_database)
    
[t1 ,t2] >> t3