from myApp import app, post_store, models
from flask import jsonify, abort, request


@app.route("/api/topic/all")
def api_topic_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)


@app.route("/api/topic/show/<int:id>")
def api_topic_show(id):
    try:
        post = post_store.get_by_id(id)
        result = jsonify(post.__dict__())
    except AttributeError:
        result = abort(404, f"topic id : {id} not exist")

    return result


@app.route("/api/topic/add", methods=["POST"])
def api_topic_add():
    request_data = request.get_json()
    try:
        new_post = models.Post(request_data["title"], request_data["content"])
        post_store.add(new_post)
        result = jsonify(new_post.__dict__())
    except ValueError:
        result = abort(400, f"Couldn't parse request data!")

    return result


@app.route("/api/topic/update/<int:id>", methods=["PUT"])
def api_topic_update(id):
    request_data = request.get_json()
    post = post_store.get_by_id(id)
    try:
        post.title = request_data["title"]
        post.content = request_data["content"]
        post_store.update(post)
        result = jsonify(post.__dict__())
    except KeyError:
        result = abort(400, f"Couldn't parse request data!")
    except AttributeError:
        result = abort(404, f"topic id: {id} doesn't exist")

    return result


@app.route("/api/topic/delete/<int:id>", methods=["DELETE"])
def api_topic_delete(id):
    try:
        post = post_store.delete(id)
        result = jsonify(post.__dict__())
    except ValueError:
        result = abort(404, f"topic id: {id} doesn't exist")

    return result


@app.errorhandler(400)
def error_request(error):
    return jsonify(message=error.description)
