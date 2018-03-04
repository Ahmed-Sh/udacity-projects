from flask import Flask, render_template
from Forums import models
from Forums import store

app = Flask(__name__)

post_store = store.PostStore()
post_store.add(models.Post('Udacity', 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor \
                    mauris condimentum nibh, ut fermentum massa justo sit amet risus.'))
post_store.add(models.Post('Flask-Project', 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor \
                    mauris condimentum nibh, ut fermentum massa justo sit amet risus.'))
post_store.add(models.Post('1MAC Full Stack', 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor \
                    mauris condimentum nibh, ut fermentum massa justo sit amet risus.'))


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=post_store.get_all())


app.run(debug=True, port=8000)
