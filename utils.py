import json
from json import JSONDecodeError


def get_posts_all():
    """возвращает посты"""
    try:
        with open("data/data.json", "r", encoding='utf8') as file:
            dict_posts = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        return "Файл не найден"
    else:
        if list(dict_posts):
            return dict_posts
        else:
            "Не удается преобразовать в словарь"


dict_json = get_posts_all()


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя"""
    user_name = user_name.lower()
    posts_list = []
    for i in dict_json:
        if user_name in i["poster_name"]:
            posts_list.append(i)
        else:
            continue
    return posts_list


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста"""
    list_comments = []
    try:
        with open("data/comments.json", "r", encoding='utf8') as file:
            dict_comment = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        return "Файл не найден"
    for p in dict_comment:
        if post_id == p["post_id"]:
            list_comments.append(p["comment"])
        else:
            continue
    if len(list_comments) >= 1:
        return list_comments
    else:
        return "Поста с таким номером не существует"


def search_for_posts(query):
    """возвращает список постов по ключевому слову"""
    word = [i.lower() for i in query.split(" ")]
    if word:
        list_content = []
        for c in word:
            for n in dict_json:
                if c in n["content"].lower():
                    list_content.append(n)
                else:
                    continue
        return list_content
    else:
        return False


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    for post in dict_json:
        if pk == post["pk"]:
            return post
