import time
import certifi
import paho.mqtt.client as mqtt
import creds


class SolaceClient:
    def __init__(self, name):
        self.name = name


# Callback on connection
def on_connect(client, userdata, flags, rc):
    print(f'Connected (Result: {rc})')
    client.subscribe('my/topic')


def on_message(client, userdata, msg):
    print(f'Message received on topic: {msg.topic}. Message: {msg.payload}')


client = mqtt.Client(transport='websockets')
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(ca_certs=certifi.where())

client.username_pw_set('solace-cloud-client', creds.PASSWORD)
client.connect('mr-connection-brdco6qtfz5.messaging.solace.cloud', port=8443)

client.loop_start()

while True:
    client.publish('my/topic', 'hello world')

    time.sleep(1.0)
