from utils import get_posts_all


def test_get_all_posts_check():
    posts = get_posts_all()
    assert type(posts) == list, "Список постов должен быть list"
    first_items = posts[0]
    excepted_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    first_items_keys = set(first_items.keys())
    assert first_items_keys == excepted_keys, "Полученные ключи неверны!"


def test_get_id_posts_check():
    posts = get_posts_all()
    assert type(posts[0]) == dict, "Пост должен быть dict"
    first_items = posts[0]
    excepted_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    first_items_keys = set(first_items.keys())
    assert first_items_keys == excepted_keys, "Полученные ключи неверны!"
