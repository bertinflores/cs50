from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    number = random.randint(0,1)
    return render_template('index.html', number = number)

@app.route("/bye")
def bye():
    return 'Goodbye!'

@app.route('/something')
def some_method():
    return 'testing extension'