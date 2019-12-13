import paho.mqtt.client as mqtt


class Storage:
    def __init__(self, host, port):
        self.mqttc = mqtt.Client()
        self.mqttc.connect(host, port=port, keepalive=60)

    def store_data(self, data):
        self.mqttc.reconnect()
        self.mqttc.publish(topic="v1/devices/me/telemetry", payload=data)

    def close(self):
        self.mqttc.disconnect()
