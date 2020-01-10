from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.items_model import ItemsModel


class Item(Resource):
    # belongs to class itself
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
        data = ItemsModel.get(_id)

        if data:
            data.delete()
            return {"message": "Item deleted"}, 200
        else:
            return {"message": "Item not found, can't delete"}, 400

    def get(self, _id):
        try:
            int(_id)
        except ValueError:
            return {"message": "Bad id format"}, 400

        item = ItemsModel.get(_id)

        if item:
            return item.jsonify(), 200
        else:
            return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, _id):
        try:
            int(_id)
        except ValueError:
            return {"message": "Bad id format"}, 400

        if ItemsModel.get(_id):
            return {"message": "Item with id '{}' already exists in database".format(_id)}, 400

        data = Item.parser.parse_args()
        item = ItemsModel(_id, **data)

        item.save()

        return item.jsonify(), 201

    @jwt_required()
    def put(self, _id):
        try:
            int(_id)
        except ValueError:
            return {"message": "Bad id format"}, 400

        data = Item.parser.parse_args()

        item = ItemsModel.get(_id)
        code = 0

        if item:
            item.id = _id
            item.name = data["name"]
            item.price = data["price"]
            item.description = data["description"]
            code = 200
        else:
            item = ItemsModel(_id, **data)
            code = 201

        item.save()

        return item.jsonify(), code
