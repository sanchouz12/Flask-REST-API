from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from db.items_db import ItemsDB


class Item(Resource):
    # belongs to class itself
    db = ItemsDB("items")
    parser = reqparse.RequestParser()

    parser.add_argument(
        "name",
        type = str,
        required = True,
        help = "You have to specify a name"
    )
    parser.add_argument(
        "price",
        type = float,
        required = True,
        help = "You have to specify a price"
    )
    parser.add_argument("description", type = str)

    @jwt_required()
    def delete(self, _id):
        data, code = Item.db.delete(_id)

        if code is None:
            return {"message": "Item deleted"}
        else:
            return data, code

    def get(self, _id):
        try:
            int(_id)
        except ValueError:
            return {"message": "Bad id format"}, 400

        item, code = Item.db.get(_id)

        return item, code

    @jwt_required()
    def post(self, _id):
        try:
            int(_id)
        except ValueError:
            return {"message": "Bad id format"}, 400

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
    def put(self, _id):
        try:
            int(_id)
        except ValueError:
            return {"message": "Bad id format"}, 400
        
        data = Item.parser.parse_args()

        item, code = Item.db.get(_id)

        if code == 200:
            item.update(data)
            Item.db.update(item, _id)
        else:
            item = {
                "id": _id,
                "name": data["name"],
                "price": data["price"],
                "description": data["description"]
            }
            Item.db.add(item)

            code = 201

        return item, code
