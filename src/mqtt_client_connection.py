import paho.mqtt.client as mqtt

from src.callbacks import on_message, on_connect, on_subscribe


class MqttClientConnection:
    def __init__(self,
                 broker_ip: str,
                 port: int,
                 username: str,
                 password: str,
                 keepalive: int = 60,
                 ):
        self._broker_ip = broker_ip
        self._port = port
        self._username = username
        self._password = password
        self._keepalive = keepalive

    def start_connection(self):
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
        client.username_pw_set(self._username, self._password)
        client.connect(self._broker_ip, self._port)

        self.connect_callbacks(client)
        client.subscribe("mytopic/topic")
        client.loop_forever()

    @staticmethod
    def connect_callbacks(client: mqtt.Client):
        client.on_message = on_message
        client.on_connect = on_connect
        client.on_subscribe = on_subscribe
