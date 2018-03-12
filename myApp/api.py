from myApp import app, post_store, models
from flask import jsonify, abort, request


@app.route("/api/topic/all")
def api_topic_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)



