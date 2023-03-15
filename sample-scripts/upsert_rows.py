# https://stackoverflow.com/questions/72071750/how-to-perform-the-upsert-operation-using-the-python-bigquery-client-when-writin

import os
from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()
client = bigquery.Client()

project_name = os.environ.get('PROJECT_NAME')
dataset_name = os.environ.get('DATASET_NAME')
original_table_name = "original_neko"
source_table_name = "source_neko"

original = f"{project_name}.{dataset_name}.{original_table_name}"
source = f"{project_name}.{dataset_name}.{source_table_name}"

sql = (

    f'MERGE {original} T \
    USING {source} S \
    ON T.id = S.id \
    WHEN MATCHED THEN \
    UPDATE SET name = S.name \
    WHEN NOT MATCHED THEN \
    INSERT (id, name) VALUES(id, name)'

)

query_job = client.query(sql)
results = query_job.result()

"""
When you run this script, ensure to let the time to pass more than 30 minutes once a table is created.
Otherwise, you will get an error:
google.api_core.exceptions.BadRequest: 400 UPDATE or DELETE statement over table would affect rows in the streaming buffer, which is not supported
"""
