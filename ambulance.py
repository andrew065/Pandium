from flask import Flask, render_template, request
import mqtt, creds

app = Flask(__name__)
ambu_client = mqtt.SolaceClient('ambu1', "llgr44bsrp3qn6jq54689ke2p9", creds.SECURED_MQTT_HOST, "", "", 'H1')
ambu_client.initialize_client()


@app.route('/', methods=['POST', 'GET'])
def index():
    # if request.method == 'POST':


    return render_template('index_ambu.html')


if __name__ == '__main__':
    app.run(debug=True)
