from db import db


class UsersModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_by_id(cls):
        db.session.delete(cls)
        db.session.commit()

    @classmethod
    def get_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    @classmethod
    def get_by_name(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def jsonify(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
        }
