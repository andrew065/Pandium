from flask import Flask, render_template, url_for, request
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ambulance', methods=['POST', 'GET'])
def ambulance():
    if request.method == 'POST':
        request.form
        print('button clicked')
        return render_template('index_ambu.html')
    else:
        return render_template('index_ambu.html')


@app.route('/hospital')
def hospital():
    return render_template('index_hosp.html')


@app.route('/publish')
def publish():  # make endpoint and fetch during button press
    print('button clicked')


if __name__ == '__main__':
    app.run(debug=True)
