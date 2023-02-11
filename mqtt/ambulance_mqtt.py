import time
import mqtt
import creds

ambu_client = mqtt.SolaceClient('ambu1', creds.PASSWORD, creds.SECURED_MQTT_HOST, ['my/topic'], ['my/topic'])

ambu_client.initialize_client()  # initialize client

while True:
    msg = input("> ")
    ambu_client.publish(0, msg)
    time.sleep(1)

    'name/GPS/ambu_num/lat/long/destination -> name/GPS/+/+/+/'
    'name/vitals/ambu_num/pulse/BP/O2_sat/status/diagnosis/message -> name/vitals/#'



