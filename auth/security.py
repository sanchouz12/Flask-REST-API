# safe string compare
from werkzeug.security import safe_str_cmp
from db.users_db import UsersDB

db = UsersDB("users")


def authenticate(username, password):
    user = db.get_by_name(username)

    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload["identity"]

    return db.get_by_id(user_id)
