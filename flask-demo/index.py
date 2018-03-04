from flask import Flask, render_template

app = Flask(__name__)

from Forums import models_data


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=models_data.post_store.get_all())


app.run(debug=True, port=8000)
