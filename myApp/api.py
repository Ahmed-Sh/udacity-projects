from myApp import app, post_store
from flask.json import jsonify


@app.route("/api/topic/all")
def topic_api_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)