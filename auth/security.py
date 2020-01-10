# safe string compare
from werkzeug.security import safe_str_cmp
from models.users_model import UsersModel

# If resource method uses "@jwt_requitred"
# "identity" would receive returned from
# "authenticate" object and would search for id
# (seems, by default, but I'm not sure)

def authenticate(username, password):
    user = UsersModel.get_by_name(username)

    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload["identity"]

    return UsersModel.get_by_id(user_id)
