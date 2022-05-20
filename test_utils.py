from utils import get_posts_all, get_comments_by_post_id
import pytest

get_json = get_posts_all()


def test_key_get_comments_by_post_id():
    with pytest.raises(KeyError):
        get_comments_by_post_id(100, "data/data.json")


def test_type_get_comments_by_post_id():
    with pytest.raises(TypeError):
        get_comments_by_post_id("2", {1})
