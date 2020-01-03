from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from dotenv import load_dotenv
import os

from security import authenticate, identity

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
api = Api(app)

# /auth
# returns token, if everything is ok
jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    # belongs to class itself
    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type = float,
                        required = True,
                        help = "You have to specify a price"
                        )
    parser.add_argument("name",
                        type = str,
                        required = True,
                        help = "You have to specify a name"
                        )
    parser.add_argument("description", type = str)

    def get(self, item_id):
        # bad request
        try:
            int(item_id)
        except ValueError:
            return {"message": "Bad id format"}, 400

        item = next(filter(lambda x: str(x["id"]) == item_id, items), None)

        return {"item": item}, 200 if item else 404

    @jwt_required()
    def post(self, item_id):
        try:
            int(item_id)
        except ValueError:
            return {"message": "Bad id format"}, 400

        if next(filter(lambda x: str(x["id"]) == item_id, items), None):
            return {"message": "Item with id '{}' already exists".format(item_id)}, 400

        data = Item.parser.parse_args()

        item = {
            "id": item_id,
            "name": data["name"],
            "price": data["price"],
            "description": data["description"]
        }
        items.append(item)

        return {"item": item}, 201

    @jwt_required()
    def delete(self, item_id):
        global items
        items = list(filter(lambda x: x["id"] != item_id, items))

        return {"message": "Item deleted"}

    @jwt_required()
    def put(self, item_id):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x["id"] == item_id, items), None)

        if item:
            item.update(data)
        else:
            item = {
                "id": item_id,
                "name": data["name"],
                "price": data["price"],
                "description": data["description"]
            }
            items.append(item)

        return {"item": item}


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<string:item_id>")
api.add_resource(ItemList, "/items")

app.run(port = 5000, debug = True)
