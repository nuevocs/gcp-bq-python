import os
from dotenv import load_dotenv
from google.cloud import pubsub_v1
import json

load_dotenv()

project_id = os.environ.get('PROJECT_NAME')
topic_name = os.environ.get('TOPIC_NAME')

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path(project_id, topic_name)
data = {"key1": "pikachu", "neko": "dora"}

json_data = json.dumps(data).encode("utf-8")

future = publisher.publish(topic_path, data=json_data)
future.result()
print(topic_path, data)