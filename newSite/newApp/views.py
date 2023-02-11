from django.shortcuts import render
# Create your views here.
import paho.mqtt.client as mqtt
from django.http import HttpResponse

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    client.subscribe("topic")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def receive_messages(request):
    client = mqtt.Client(transport = "websockets")
    client.on_connect = on_connect

    print("connected")
    client.on_message = on_message
    print("messaged")
    client.username_pw_set("solace-cloud-client", "llgr44bsrp3qn6jq54689ke2p9")
    print("up set")
    client.connect('mr-connection-brdco6qtfz5.messaging.solace.cloud', port=8443)
    print("connected                 ------")
    client.loop_start()
    #return render(request, 'index.html')
    return HttpResponse("Connected to MQTT broker.")
