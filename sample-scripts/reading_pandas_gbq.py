import pandas_gbq
import os
from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()
client = bigquery.Client()

project_name = os.environ.get('PROJECT_NAME')
dataset_name = os.environ.get('DATASET_NAME')
table_name = "xxxtable"

sql = (
    f'SELECT * FROM `{project_name}.{dataset_name}.{table_name}` LIMIT 10'
)


df = pandas_gbq.read_gbq(sql, project_id=project_name)

print(df)