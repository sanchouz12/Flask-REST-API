from flask_restful import Resource
from models.items_model import ItemsModel


class ItemList(Resource):
    def get(self):
        return ItemsModel.get_all()
