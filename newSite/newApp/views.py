from django.shortcuts import render
# Create your views here.
import paho.mqtt.client as mqtt
import certifi
from django.http import HttpResponse
import random as rand
import csv
msgO = ""
cnt = 0
def on_connect(client, userdata, flags, rc):

    print("Connected with result code "+str(rc))
    client.subscribe("+/topic")

def on_message(client, userdata, msg):
    msgO = str(msg.payload)
    print(msg.topic+" "+str(msg.payload))

def receive_messages(request):

    client = mqtt.Client(transport = "websockets")
    client.on_connect = on_connect

    print("connected")
    client.on_message = on_message
    print("messaged")
    client.tls_set(ca_certs=certifi.where())

    client.username_pw_set("solace-cloud-client", "llgr44bsrp3qn6jq54689ke2p9")
    print("up set")
    client.connect('mr-connection-brdco6qtfz5.messaging.solace.cloud', port=8443)
    print("connected                 ------")
    client.loop_start()
    #return render(request, 'index.html')

    return HttpResponse(rand.random())

