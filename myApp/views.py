<<<<<<< HEAD
from flask import render_template, request, redirect, url_for
from myApp import app, post_store
from myApp import models


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=post_store.get_all())


@app.route("/topic/view/<int:id>")
def topic_view(id):
    post = post_store.get_by_id(id)
    if post is not None:
        return render_template("topic_view.html", post=post)
    return redirect(url_for("home"))


@app.route("/topic/add", methods=["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))
    else:
        return render_template("topic_add.html")


@app.route("/topic/edit/<int:id>", methods=["GET", "POST"])
def topic_edit(id):
    post = post_store.get_by_id(id)
    if post is not None:
        if request.method == "POST":
            post.title = request.form['title']
            post.content = request.form['content']
            post_store.update(post)
            return render_template("topic_edit.html", post=post)
        else:
            return render_template("topic_edit.html", post=post)
    return redirect(url_for("home"))


@app.route("/topic/delete/<int:id>")
def topic_delete(id):
    if post_store.get_by_id(id) is not None:
            post_store.delete(id)
    return redirect(url_for("home"))
|||||||
=======
from flask import render_template, request, redirect, url_for
from myApp import app, post_store, models


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
>>>>>>> 1.0.0
