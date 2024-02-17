import configparser
from src.mqtt import MqttClientConnection


def load_configurations(file_name):
    config = configparser.ConfigParser()
    config.read(file_name)
    return config["MQTT_BROKER"]


def start():
    configurations = load_configurations('config.ini')

    mqtt_client_connection = MqttClientConnection(
        configurations["HOST"],
        int(configurations["PORT"]),
        configurations["USERNAME"],
        configurations["PASSWORD"],
        int(configurations["KEEPALIVE"]),
    )
    mqtt_client_connection.start_connection()


if __name__ == "__main__":
    start()
