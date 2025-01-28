from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("main.html")


@app.route("/calculate")
def show_calc_form():
    return render_template("calculator.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    number = int(request.form["number"])
    result = number**2
    return render_template('calculator.html', result=result)