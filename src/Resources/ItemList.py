from flask_restful import Resource
from src.db.items_db import ItemsDB


class ItemList(Resource):
    db = ItemsDB("items")

    def get(self):
        items = ItemList.db.get_all()
        return items
