from flask_restful import Resource
from models.stores_model import StoresModel

class Store(Resource):
    def get(self, name):
        store = StoresModel.get_by_name(name)

        if store:
            return store.jsonify(), 200
        else:
            return {"message": "Store not found"}, 404

    def post(self, name):
        if StoresModel.get_by_name(name):
            return {"message": "Store with name {} already exists".format(name)}, 400
        else:
            store = StoresModel(name)

            store.save()

        return store.jsonify()

    def delete(self, name):
        store = StoresModel.get_by_name(name)

        if store:
            store.delete()

            return {"message": "Store was deleted"}, 200
        else:
            return {"message": "Store not found"}, 400