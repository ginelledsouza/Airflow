from airflow.models import Variable

post_config = Variable.get("Access Credential", deserialize_json=True)

# Database links and creds (PostgreSQL)
user = post_config['user'] 
password = post_config['password'] 
host = post_config['host'] 
port = post_config['port'] 
database = post_config['database'] 