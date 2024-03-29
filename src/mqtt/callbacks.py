from src.mongo import mongo_manager
from src.sqs import queue, sqs_manager


def on_connect(client, obj, flags, reason_code, properties):
    print("reason_code: " + str(reason_code))


def on_message(client, obj, msg):
    mongo_manager.insert_document({"data": str(msg.payload)})
    sqs_manager.send_message(queue, str(msg.payload))
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_subscribe(client, obj, mid, reason_code_list, properties):
    print("Subscribed: " + str(mid) + " " + str(reason_code_list))


def on_log(client, obj, level, string):
    print(string)
