from flask_restful import Resource, reqparse
from src.db.users_db import UsersDB


class RegUser(Resource):
    parser = reqparse.RequestParser()
    db = UsersDB("users")

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

        RegUser.db.add(data)

        return {"message": "User was created"}, 201
