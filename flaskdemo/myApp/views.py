from flask import render_template, request, redirect, url_for
from flaskdemo.myApp import app, post_store, models


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=post_store.get_all())


@app.route("/topic/view/<int:id>")
def topic_view(id):
    post = post_store.get_by_id(id)
    return render_template("topic_view.html", post=post)


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
    if request.method == "POST":
        post.title = request.form['title']
        post.content = request.form['content']
        post_store.update(post)
        return redirect(url_for("home"))
    else:
        return render_template("topic_edit.html", post=post)


@app.route("/topic/delete/<int:id>")
def topic_delete(id):
    post_store.delete(id)
    return redirect(url_for("home"))