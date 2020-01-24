from db import db


class StoresModel(db.Model):
    __tablename__ = "store"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    items = db.relationship("ItemsModel", lazy = "dynamic")

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_name(cls, name):
        store = cls.query.filter_by(name = name).first()

        return store

    @classmethod
    def get_all(cls):
        stores = [
            store.jsonify()
        for store in cls.query.all()]

        return {"stores": stores}

    def jsonify(self):
        return {
            "name": self.name,
            "items": [item.jsonify() for item in self.items.all()]
        }
