import time

from configs import mqtt_broker_configs
from src.mqtt_client_connection import MqttClientConnection


def start():
    mqtt_client_connection = MqttClientConnection(
        mqtt_broker_configs["HOST"],
        mqtt_broker_configs["PORT"],
        mqtt_broker_configs["USERNAME"],
        mqtt_broker_configs["PASSWORD"],
        mqtt_broker_configs["KEEPALIVE"],
    )
    mqtt_client_connection.start_connection()

    while True: time.sleep(0.001)


if __name__ == "__main__":
    start()
