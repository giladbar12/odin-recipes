from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lasagna')
def lasagna():
    return render_template('recipes/lasagna.html')

@app.route('/pizza')
def pizza():
    return render_template('recipes/pizza.html')

@app.route('/brownies')
def brownies():
    return render_template('recipes/brownies.html')