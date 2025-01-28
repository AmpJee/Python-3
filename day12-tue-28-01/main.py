from flask import Flask, render_template, request
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
import os

UPLOAD_FOLDER = 'static/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("plotter.html")


# @app.route("/calculate")
# def show_calc_form():
#     return render_template("calculator.html")


# @app.route("/calculate", methods=["POST"])
# def calculate():
#     number = int(request.form["number"])
#     result = number**2
#     return render_template('calculator.html', result=result)


@app.route("/plot", methods=["GET", "POST"])
def plot():
    if request.method == "GET":
        return render_template('plotter.html')
    elif request.method == "POST":
        function = request.form['func']
        start = int(request.form["start"])
        end = int(request.form["end"])
        print(len(function))
        x = np.linspace(start, end, 100)
        if function == "linear":
            y = x
        elif function == "sine":
            y = np.sin(x)
        elif function == "cosine":
            y = np.cos(x)
        elif function == "exponential":
            y = np.exp(x)
        elif function == "logarithmic":
            y = np.log(x)
        plt.plot(x,y, color='blue')
        plt.savefig('static/plot.png')
        plt.close()
        return render_template('plotter.html', plot_url='static/plot.png')


@app.route("/plotHistogram", methods=["GET", "POST"])
def plotHistogram():
    if request.method == "GET":
        return render_template('plotter.html')
    elif request.method == "POST":
        file = request.files['csvFile']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        data = np.loadtxt(f"static/{file.filename}", delimiter=',')
        plt.hist(data, bins=10)
        plt.savefig('static/plot.png')
        return render_template('plotter.html', plot_url='static/plot.png')