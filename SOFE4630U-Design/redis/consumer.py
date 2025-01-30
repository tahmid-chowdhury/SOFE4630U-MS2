
from google.cloud import pubsub_v1
import redis
import base64
import os

ip="34.118.128.245"
r = redis.Redis(host=ip, port=6379, db=0, password='sofe4630u')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\tahmi\Documents\Cloud Computing\Project Milestone 2\SOFE4630U-MS2\SOFE4630U-Design\redis\tahmids-project-95921-bffa952bdc6d.json"
project_id = "tahmids-project-95921"
subscription_id = "images-sub"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

r = redis.Redis(host="localhost", port=6379, db=0)

def callback(message):
    image_name = message.attributes.get("filename", "unknown.png")
    image_data = base64.b64decode(message.data.decode("utf-8"))
    r.set(image_name, image_data)
    message.ack()

future = subscriber.subscribe(subscription_path, callback=callback)
print("Listening for image messages...")
future.result()