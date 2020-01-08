from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from dotenv import load_dotenv
import os

from auth.security import authenticate, identity
from Resources.Item import Item
from Resources.ItemList import ItemList
from Resources.RegUser import RegUser

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
api = Api(app)

# /auth
# returns token, if everything is ok
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:_id>")
api.add_resource(ItemList, "/items")
api.add_resource(RegUser, "/register")

if __name__ == "__main__":
    app.run(port = 5000, debug = True)
