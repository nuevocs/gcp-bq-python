import os

from google.cloud import bigquery
from dotenv import load_dotenv
load_dotenv()
client = bigquery.Client()

project_name = os.environ.get('PROJECT_NAME')
dataset_name = os.environ.get('DATASET_NAME')


QUERY = (
    f'SELECT * FROM `{project_name}.{dataset_name}.laptopprice` LIMIT 10'
)
query_job = client.query(QUERY)
rows = query_job.result()

for row in rows:
    print(row)