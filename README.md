# Orchestrate data flow with AIRFLOW!
Airflow utilizes directed acyclic graphs (DAGs) to manage the orchestration of a workflow. 
DAG consists of tasks and tasks dependencies. They are concerned with task execution, the order to run them, and execute retries if a 
task has timed out. A DAG can be triggered at a specific time or based on an external trigger. Airflow concepts are vast. Therefore, 
we will touch upon certain areas like

1. Storing variables and connections
2. Using multiple scripts
3. DAG scheduler
4. Generating email if an error

## File Structure 
The file must be stored as follows within the airflow "dags" folder.<br>
![Airflow Structure](https://user-images.githubusercontent.com/64312327/159173544-a944a9dd-2b64-4824-bf2a-7a1731fc0b05.jpg)