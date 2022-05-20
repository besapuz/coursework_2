import logging

from flask import Flask, Blueprint, jsonify

from utils import get_posts_all, get_post_by_pk

app = Flask(__name__)
api_blueprint = Blueprint('api_blueprint', __name__)
logging.basicConfig(level=logging.INFO)


@api_blueprint.route("/api/posts/", methods=['GET'])
def index_page():
    logging.debug("Получены все данные через API")
    return jsonify(get_posts_all())


@api_blueprint.route("/api/posts/<post_id>", methods=['GET'])
def page_tag(post_id):
    try:
        post_id = int(post_id)
        logging.info(f"Получены данные {post_id} пользователя")
    except ValueError:
        logging.info("Ошибка формата")
        return "Введите целое число"
    else:
        content = get_post_by_pk(post_id)
        return jsonify(content)


if __name__ == "__main__":
    app.run(port=60)
