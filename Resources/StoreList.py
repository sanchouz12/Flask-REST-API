from flask_restful import Resource
from models.stores_model import StoresModel

class StoreList(Resource):
    def get(self):
        return StoresModel.get_all()
