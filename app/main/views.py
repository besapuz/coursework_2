import logging

from flask import Blueprint, render_template

from utils import get_posts_all

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="info.log", level=logging.INFO)


@main_blueprint.route("/", methods=['GET'])
def index_page():
    logging.info("Открыта главная страница")
    return render_template('index.html', posts_all=get_posts_all())
