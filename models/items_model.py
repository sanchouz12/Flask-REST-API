from db import db


class ItemsModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))
    description = db.Column(db.String(300))

    def __init__(self, _id, name, price, description):
        self.id = _id
        self.name = name
        self.price = price
        self.description = description

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get(cls, _id):
        item = cls.query.filter_by(id = _id).first()

        return item

    @classmethod
    def get_all(cls):
        items = [
            item.jsonify()
        for item in cls.query.all()]
        
        return {"items": items}

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description
        }
