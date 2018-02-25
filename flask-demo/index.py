from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    return "Hello Everyone"


@app.route("/SayHello/<name>")
def say_hello(name):
    return f"Hello {name}"


app.run()
