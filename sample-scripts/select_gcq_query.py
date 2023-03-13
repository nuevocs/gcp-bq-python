from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()
client = bigquery.Client()

QUERY = (
    'SELECT * FROM `xenon-momentum-363005.mydev.laptopprice` LIMIT 10'
)
query_job = client.query(QUERY)
rows = query_job.result()

for row in rows:
    print(row)
