import paho.mqtt.client as mqtt

from src import config
from src.mqtt.callbacks import on_message, on_connect, on_subscribe


class MqttClientManger:
    def __init__(self, config):
        self._broker_ip = config["HOST"]
        self._port = int(config["PORT"])
        self._username = config["USERNAME"]
        self._password = config["PASSWORD"]
        self._keepalive = int(config["KEEPALIVE"])

    def start_connection(self):
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
        client.username_pw_set(self._username, self._password)
        client.connect(self._broker_ip, self._port)

        self.connect_callbacks(client)
        client.subscribe("topic/topic")
        client.loop_forever()

    @staticmethod
    def connect_callbacks(client: mqtt.Client):
        client.on_message = on_message
        client.on_connect = on_connect
        client.on_subscribe = on_subscribe


mqtt_manager = MqttClientManger(config["MQTT_BROKER"])
