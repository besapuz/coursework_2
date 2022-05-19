from utils import get_posts_all, get_comments_by_post_id
import pytest


def test_get_list_dict():
    get_json = get_posts_all()
    assert type(get_json) == list, "Не являтся списком"
    assert type(get_json[0]) == dict, "Не является словарем"


def test_key_error():
    with pytest.raises(KeyError):
        get_comments_by_post_id(2, "data/data.json")


def test_value_error():
    with pytest.raises(TypeError):
        get_comments_by_post_id("2", {1})