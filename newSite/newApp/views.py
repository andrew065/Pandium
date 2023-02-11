from django.shortcuts import render
# Create your views here.
import paho.mqtt.client as mqtt
from django.http import HttpResponse

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("mqtt_topic")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def receive_messages(request):
    client = mqtt.Client()
    client.on_connect = on_connect
    print("connected")
    client.on_message = on_message
    print("messaged")
    client.username_pw_set("solace-cloud-client", "llgr44bsrp3qn6jq54689ke2p9")
    print("up set")
    client.connect("172.19.0.2", 8000, 60)
    print("connected                 ------")
    client.loop_start()
    #return render(request, 'index.html')
    return HttpResponse("Connected to MQTT broker.")
