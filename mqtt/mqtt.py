import paho.mqtt.client as mqtt
import creds
import ssl

client = mqtt.Client(client_id='hos1', clean_session=False)

client.username_pw_set(username=creds.USERNAME, password=creds.PASSWORD)
client.connect('tcps://mr-connection-brdco6qtfz5.messaging.solace.cloud:8443', port=8080, keepalive=60, bind_address="")
client.loop_start()

client.publish('my/topic', 'hello world')
client.subscribe('my/topic')


def on_message(client, usr_data, msg):
    print(f'Received message on topic: {msg.topic}. Message: {msg.payload.decode("utf-8")}')


client.on_message = on_message

while True:
    pass
