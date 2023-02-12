from flask import Flask, render_template
import mqtt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('hospital.html')


# @app.route('/position')
# def position():
#     return {45.62, -75}


def on_message(client, msg):
    print(str(msg.payload))

# @app.route('/sub')
# def on_message(client, userdata, msg):
#     if str(msg.topic) == '*/gps':
#         coords = str(msg.payload).split('_')
#
#     elif str(msg.topic) == '*/vitals':
#         pass


hos_client = mqtt.SolaceClient("h1", "", ['*/gps', '*/vitals'], "")
hos_client.initialize_client()
hos_client.subscribe()
hos_client.client.on_message = on_message


if __name__ == '__main__':
    app.run(debug=True)

