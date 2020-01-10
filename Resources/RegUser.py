from flask_restful import Resource, reqparse
from models.users_model import UsersModel


class RegUser(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("username",
                        type = str,
                        required = True,
                        help = "You have to specify a username")
    parser.add_argument("password",
                        type = str,
                        required = True,
                        help = "You have to specify a password")

    def post(self):
        data = RegUser.parser.parse_args()

        if UsersModel.get_by_name(data["username"]):
            return {"message": "User with that username already exists"}, 400

        user = UsersModel(None, **data)
        user.save()

        return {"message": "User was created"}, 201
