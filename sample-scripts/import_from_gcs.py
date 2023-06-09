import os
from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()
client = bigquery.Client()

project_name = os.environ.get('PROJECT_NAME')
dataset_name = os.environ.get('DATASET_NAME')

table_ref = f"{project_name}.{dataset_name}.xxxtable"

job_config = bigquery.LoadJobConfig()
job_config.skip_leading_rows = 1
job_config.source_format = bigquery.SourceFormat.CSV

bucket_name = "nuevocs-storage"
uri = f"gs://{bucket_name}/mycsv.csv"

load_job = client.load_table_from_uri(
    uri,
    table_ref,
    job_config=job_config
)

load_job.result()