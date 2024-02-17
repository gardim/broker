import configparser


def load_configurations(file_name):
    config_setup = configparser.ConfigParser()
    config_setup.read(file_name)
    return config_setup


config = load_configurations("config.ini")
