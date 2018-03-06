from flask import Flask, render_template, request, redirect, url_for
import models, store, models_data

app = Flask(__name__)


member_store = store.MemberStore()
post_store = store.PostStore()


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=post_store.get_all())


@app.route("/topic/add", methods=["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))
    else:
        return render_template("topic_add.html")


if __name__ == '__main__':
    models_data.add_stores(post_store, member_store)
    app.run(debug=True, port=8000)
