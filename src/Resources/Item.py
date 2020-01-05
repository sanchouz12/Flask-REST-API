from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from src.db.items_db import ItemsDB


class Item(Resource):
    # belongs to class itself
    db = ItemsDB("items")
    parser = reqparse.RequestParser()

    parser.add_argument("name",
                        type = str,
                        required = True,
                        help = "You have to specify a name"
                        )
    parser.add_argument("price",
                        type = float,
                        required = True,
                        help = "You have to specify a price"
                        )
    parser.add_argument("description", type = str)

    @jwt_required()
    def delete(self, item_id):
        items = list(filter(lambda x: x["id"] != item_id, Item.items))

        return {"message": "Item deleted"}

    def get(self, _id):
        # bad request
        try:
            int(_id)
        except ValueError:
            return {"message": "Bad id format"}, 400

        item, code = Item.db.get(_id)

        return item, code

    @jwt_required()
    def post(self, _id):
        if Item.db.get(_id)[1] == 200:
            return {"message": "Item with id '{}' already exists in database".format(_id)}, 400

        data = Item.parser.parse_args()
        item = {
            "id": _id,
            "name": data["name"],
            "price": data["price"],
            "description": data["description"]
        }

        item, code = Item.db.add(item)

        return item, code

    @jwt_required()
    def put(self, item_id):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x["id"] == item_id, Item.items), None)

        if item:
            item.update(data)
        else:
            item = {
                "id": item_id,
                "name": data["name"],
                "price": data["price"],
                "description": data["description"]
            }
            Item.items.append(item)

        return {"item": item}
