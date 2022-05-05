# Orchestrate data flow with AIRFLOW!
Airflow utilizes directed acyclic graphs (DAGs) to manage the orchestration of a workflow. 
DAG consists of tasks and tasks dependencies. They are concerned with task execution, the order to run them, and execute retries if a 
task has timed out. A DAG can be triggered at a specific time or based on an external trigger. Airflow concepts are vast. Therefore, 
we will touch upon certain areas like

1. Storing variables and connections<br>
   1.1 Variables<br>
	   1.1.1 Airflow Webserver User Interface<br>
	   1.1.2 Command Line Interface<br>
	   1.1.3 Python Code<br>
   1.2 Connections<br>
2. Using multiple scripts<br>
3. DAG scheduler<br>
   3.1 String Expression<br>
   3.2 CRON expression<br>
4. Generating email<br>
   4.1 Setting up an SMTP connection in ```airflow.cfg``` [Using a Gmail Agent]<br>
   4.2 Setting email trigger in DAG script

## File Structure 
The file must be stored as follows within the airflow "dags" folder.<br>
![Airflow Structure](https://user-images.githubusercontent.com/64312327/159173544-a944a9dd-2b64-4824-bf2a-7a1731fc0b05.jpg)

## Medium Link
A detailed explaination for all the above concepts has been given in my medium article ["Orchestrate data pipelines with Apache Airflow!"](https://levelup.gitconnected.com/orchestrate-data-pipelines-with-apache-airflow-7dae6338fe90). 
Feel free to drop by to have a better understanding of the listed concepts.
