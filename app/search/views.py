import logging

from flask import Blueprint, render_template, request

from utils import get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="info.log", level=logging.INFO)


@search_blueprint.route("/posts/<int:post_id>", methods=['GET'])
def page_tag(post_id):
    logging.info("Выполнен поиск по id")
    comments = get_comments_by_post_id(post_id, "data/comments.json")
    content = get_post_by_pk(post_id)
    len_comment = len(comments)
    return render_template('post.html', comments=comments, len_comment=len_comment, content=content)


@search_blueprint.route("/search")
def get_word_post():
    logging.info("Выполнен поиск по слову")
    word = request.args.get("s")
    content = search_for_posts(word)
    len_content = len(content)
    return render_template("search.html", content=content, word=word, len_content=len_content)


@search_blueprint.route("/users/<string:username>")
def get_name_posts(username):
    logging.info("Выполнен поиск по имени")
    user_name = get_posts_by_user(username)
    return render_template("user-feed.html", user_name=user_name)
