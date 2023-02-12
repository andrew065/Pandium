from flask import Flask, render_template
from mqtt import SolaceClient

app = Flask(__name__)


@app.route('/')
def index():
    hosClient = SolaceClient("hos1", "llgr44bsrp3qn6jq54689ke2p9")
    hosClient.initialize_client()

    #the information pass through should be processed in the MQTT file right after it is processed


    return render_template('hospital.html')


if __name__ == '__main__':
    app.run(debug=True)
