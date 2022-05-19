import logging

from flask import Blueprint, jsonify

from utils import get_posts_all, get_post_by_pk

api_blueprint = Blueprint('api_blueprint', __name__)
logging.basicConfig(filename="api.log", level=logging.INFO)


@api_blueprint.route("/api/posts/", methods=['GET'])
def index_page():
    logging.debug("Получены все данные через API")
    return jsonify(get_posts_all())


@api_blueprint.route("/api/posts/<int:post_id>", methods=['GET'])
def page_tag(post_id):
    logging.debug(f"Получены данные {post_id} пользователя")
    content = get_post_by_pk(post_id)
    return jsonify(content)
