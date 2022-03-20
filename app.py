from flask import Flask, render_template
import requests
import json

# Simple beer app to test flask using external beer api, Bulma CSS and simple scraping
app = Flask(__name__)

@app.route("/")
def get_beer():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    beer_json = r.json()
    print(beer_json[0]['name'])
    print(beer_json[0]['abv'])
    print(beer_json[0]['description'])
    print(beer_json[0]['food_pairing'][0])

    beer_dict = {
        'name': beer_json[0]['name'],
        'abv': beer_json[0]['abv'],
        'description': beer_json[0]['description'],
        'foodpair': beer_json[0]['food_pairing'][0],
    }
    return render_template('index.html', beer = beer_dict)