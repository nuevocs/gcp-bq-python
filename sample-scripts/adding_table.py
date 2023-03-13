from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()
client = bigquery.Client()

table_name = 'dora'
table_id = "xenon-momentum-363005.mydev.xxxtable"

schema = [
    bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
]


table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)