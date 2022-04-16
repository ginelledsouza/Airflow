from airflow.hooks.base_hook import BaseHook
from airflow.models import Variable
import json

f = open('Variables.json')
data = json.load(f)
Variable.set('zelle_columns_CODE',data)

post_config = Variable.get("zelle_columns", deserialize_json=True)
conn = BaseHook.get_connection('zelle_connection')

# Database links and creds (PostgreSQL)
user = conn.login
password = conn.password 
host = conn.host
port = conn.port
database = conn.schema

# Database links and creds (PostgreSQL)
filtered_col = post_config['data_columns']
