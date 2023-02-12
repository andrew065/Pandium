import certifi
import paho.mqtt.client as mqtt


class SolaceClient:
    def __init__(self, name, password, host_link="", topics="", subscriptions=[], destination=""):
        self.name = name
        self.tops = topics
        self.subs = subscriptions
        self.port = 8443
        self.password = password
        self.mqtt_host = host_link
        self.dest = destination
        self.client = mqtt.Client(transport='websockets')

        self.tempMsg = ""
        self.tempTop = ""

    def initialize_client(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.tls_set(ca_certs=certifi.where())
        self.client.username_pw_set('solace-cloud-client', self.password)
        self.client.connect(self.mqtt_host, self.port)

        self.client.loop_start()

    def on_connect(self, userdata, flags, rc):
        print(f'Connected (Result: {rc})')

    def on_message(self, userdata, msg):
        print(f'Message received on topic: {msg.topic}. Message: {msg.payload}')
        tp = self.tempTop = msg.topic
        ms = self.tempMsg = msg.payload

    def publish(self, index, msg):
        print(msg)
        self.client.publish(self.tops[index], msg)

    def publish(self, topic, msg):
        print(msg)
        self.client.publish(topic, msg)
