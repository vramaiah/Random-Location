from flask import Flask, render_template

from data import extract_data

from os import environ

from json import dumps

app = Flask(__name__)


@app.route('/')
def index():
    """The index view"""
    return render_template('index.html')


@app.route('/api/v1/get_random_city')
def get_data():
    (city, state, country) = extract_data()
    value = {'city' : city.title(), 
             'state' : state.title(), 
             'country' : country.title()}
    return dumps(value)


host = environ.get('IP_ADDRESS', default='127.0.0.1')

app.run(host=host, port=81)
