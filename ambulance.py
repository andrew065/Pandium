from flask import Flask, render_template, request
import mqtt, creds

app = Flask(__name__)
ambu_client = mqtt.SolaceClient('ambu1', creds.PASSWORD, creds.SECURED_MQTT_HOST, "", "", 'h1')
ambu_client.initialize_client()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        button_value = request.form.get('Submit Vitals') or request.form.get('Submit GPS')
        if button_value == 'Submit Vitals':
            payload = f"{request.form['pulse']}_{request.form['bp_num']}_{request.form['bp_den']}_{request.form['sat']}_{request.form['stat']}_{request.form['diagnosis']}_{request.form['message']}"
            ambu_client.publish('h1/vitals', payload)
            print(payload)
        elif button_value == 'Submit GPS':
            payload = f"{request.form['lat']}_{request.form['long']}"
            ambu_client.publish('h1/gps', payload)
            print(payload)

    return render_template('index_ambu.html')


if __name__ == '__main__':
    app.run(debug=True)
