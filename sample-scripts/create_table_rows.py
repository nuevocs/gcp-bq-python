import os
from dotenv import load_dotenv
from google.cloud import bigquery

load_dotenv()

project_name = os.environ.get('PROJECT_NAME')
dataset_name = os.environ.get('DATASET_NAME')
bucket_name = os.environ.get('BUCKET_NAME')
table_name = 'source_neko'

client = bigquery.Client()

table_id = f"{project_name}.{dataset_name}.{table_name}"

# job_config = bigquery.LoadJobConfig(
#     schema=[
#         bigquery.SchemaField("id", "INTEGER"),
#         bigquery.SchemaField("name", "STRING"),
#     ],
# )

schema = [
    bigquery.SchemaField("id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)

data = [
    {"id": 1, "name": "John"},
    {"id": 4, "name": "Taro"},
    {"id": 3, "name": "Reina"},
]

errors = client.insert_rows_json(table_id, data)
if not errors:
    print("Data inserted successfully.")
