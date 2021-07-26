from flask import Flask, Markup, redirect, render_template, url_for
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():

    data = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit")
                   .json()
                   .items()
    for key, value in data:

        if key == 'joke':
            joke = value
        elif key == 'setup':
            joke = value
        elif key == 'delivery':
            joke = Markup(joke + 3 * '<br />' + value)

    return render_template('home.html', subtitle='PLEASE ENJOY THIS JOKE', text='as told by a person that doesn\'t exist:', joke=joke)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    