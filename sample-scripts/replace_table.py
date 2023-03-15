import six
import os
from dotenv import load_dotenv
from google.cloud import bigquery
load_dotenv()

project_name = os.environ.get('PROJECT_NAME')
dataset_name = os.environ.get('DATASET_NAME')
bucket_name = os.environ.get('BUCKET_NAME')
table_name = 'doraneko'


client = bigquery.Client()

table_id = f"{project_name}.{dataset_name}.{table_name}"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING"),
    ],
)

body = six.BytesIO(b"Washington,WA")
client.load_table_from_file(body, table_id, job_config=job_config).result()
previous_rows = client.get_table(table_id).num_rows
assert previous_rows > 0

job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
)

uri = f"gs://{bucket_name}/mycsv2.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))
