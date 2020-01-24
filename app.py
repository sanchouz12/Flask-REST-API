import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from dotenv import load_dotenv

from auth.security import authenticate, identity
from Resources.Item import Item
from Resources.ItemList import ItemList
from Resources.RegUser import RegUser
from Resources.Store import Store
from Resources.StoreList import StoreList

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databases/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.secret_key = os.getenv("SECRET_KEY")
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

# /auth
# returns token, if everything is ok
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:_id>")
api.add_resource(ItemList, "/items")
api.add_resource(RegUser, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port = 5000, debug = True)
