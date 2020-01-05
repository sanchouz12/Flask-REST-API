from .helpers.connection import DBConnection
from .helpers.create_tables import create_table


class ItemsDB:
    def __init__(self, host):
        self.host = create_table(host)

    def add(self, item):
        with DBConnection(self.host) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO items VALUES (?, ?, ?, ?)"

            cursor.execute(query, (item["id"], item["name"], item["price"], item["description"]))

        return {"item": item}, 201

    def get(self, _id):
        with DBConnection(self.host) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM items WHERE id = ?"

            cursor.execute(query, (_id, ))
            data = cursor.fetchone()

        if data:
            return {"item": {
                "id": data[0],
                "name": data[1],
                "price": data[2],
                "description": data[3]
            }}, 200
        return {"message": "Item not found"}, 404

    def get_all(self):
        with DBConnection(self.host) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM items"

            cursor.execute(query)
            data = cursor.fetchall()

        items = [{
            "id": item[0],
            "name": item[1],
            "price": item[2],
            "description": item[3]
        }for item in data]

        return {"items": items}
