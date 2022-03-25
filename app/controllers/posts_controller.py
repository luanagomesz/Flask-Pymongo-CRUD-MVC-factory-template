from http.client import OK
from ..models.dev_model import post
from flask import jsonify, request
from http import HTTPStatus
from ..exceptions.posts_exc import PostNotFoundError
def get_posts():
    posts = post.get_all_posts()

    return  posts, HTTPStatus.OK

def create_post():
    req = request.get_json()

    try:
        instance = post(**req)
    except KeyError:
        return {"error": "missing key"}, HTTPStatus.BAD_REQUEST
    
    created_post = instance.create_post()
    return jsonify(created_post), HTTPStatus.CREATED

def get_post_by_id(id):
    
    response = post.get_post_by_id(id)
    if response:
        return jsonify(response), HTTPStatus.OK
    else:
        return {"error": f"post with id: {id} not found"},HTTPStatus.NOT_FOUND

def delete_post(id):
    
    try:
        response = post.delete_post(id)
        return jsonify(response),HTTPStatus.OK
    except PostNotFoundError:
        return {"error": f"post with id: {id} not found"},HTTPStatus.NOT_FOUND

def update_post(id):
    req = request.get_json()

    try:
        response = post.update_post(req, id)
        if isinstance(response, str):
            return {"error": response},HTTPStatus.BAD_REQUEST
        else:
            return jsonify(response),HTTPStatus.OK
    except PostNotFoundError:
        return {"error": f"post with id: {id} not found"},HTTPStatus.NOT_FOUND



    
