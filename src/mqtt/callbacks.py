from src.mongo import mongo_client


def on_connect(client, obj, flags, reason_code, properties):
    print("reason_code: " + str(reason_code))


def on_message(client, obj, msg):
    mongo_client.insert_document({"data": msg.payload})
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_subscribe(client, obj, mid, reason_code_list, properties):
    print("Subscribed: " + str(mid) + " " + str(reason_code_list))


def on_log(client, obj, level, string):
    print(string)
