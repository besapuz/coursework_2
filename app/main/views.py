import logging
from flask import Blueprint, render_template, request
from utils import get_comments_by_post_id, get_posts_all, get_post_by_pk, search_for_posts

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="info.log", level=logging.INFO)


@main_blueprint.route("/")
def index_page():
    logging.info("Открыта главная страница")
    return render_template('index.html', posts_all=get_posts_all())


@main_blueprint.route("/posts/<int:post_id>")
def page_tag(post_id):
    logging.info("Выполнен поиск")
    comments = get_comments_by_post_id(post_id, "data/comments.json")
    content = get_post_by_pk(post_id)
    len_comment = len(comments)
    return render_template('post.html', comments=comments, len_comment=len_comment, content=content)


@main_blueprint.route("/search")
def get_word_post():
    logging.info("Выполнен поиск")
    word = request.args.get("s")
    content = search_for_posts(word)
    len_content = len(content)
    return render_template("search.html", content=content, word=word, len_content=len_content)

