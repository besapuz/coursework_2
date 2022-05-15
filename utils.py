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


def get_comments_by_post_id(post_id, c):
    """возвращает комментарии определенного поста"""
    list_comments = []
    try:
        with open(c, "r", encoding='utf8') as file:
            dict_comment = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        return "Файл не найден"
    for p in dict_comment:
        if post_id == p["post_id"]:
            list_comments.append(p)
        else:
            continue
    return list_comments


def search_for_posts(query):
    """возвращает список постов по ключевому слову"""
    list_content = []
    try:
        query = query.lower()
    except:
        return "Вы ввели не не слово"
    else:
        count = 0
        for c in dict_json:
            if count <= 10:
                if query in c["content"].lower():
                    list_content.append(c)
                    count += 1
                else:
                    continue
        return list_content


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    for post in dict_json:
        if pk == post["pk"]:
            return post
