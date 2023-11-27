import paho.mqtt.client as mqtt

class MqttClientConnection:
    def __init__(self, Broker_ip: str, port: int, client_name: str, keepalive=60):
        self.__broker_ip = Broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive

    def start_connection(self):
        mqtt_client = mqtt.Client(  self.__client_name)
        mqtt_client.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)   
        mqtt_client.loop_start()