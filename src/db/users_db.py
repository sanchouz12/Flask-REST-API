from src.db.helpers.connection import DBConnection
from src.db.helpers.create_tables import create_table


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


class UsersDB:
    def __init__(self, host):
        self.host = create_table(host)

    def add(self, user):
        with DBConnection(self.host) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO users VALUES (NULL, ?, ?)"

            cursor.execute(query, (user["username"], user["password"]))

    def delete_by_id(self, _id):
        with DBConnection(self.host) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM users WHERE id = ?"

            cursor.execute(query, (_id, ))

    def get_by_id(self, _id):
        with DBConnection(self.host) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM users WHERE id = ?"

            cursor.execute(query, (_id, ))
            data = cursor.fetchone()

            if data:
                return User(*data)

    def get_by_name(self, username):
        with DBConnection(self.host) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM users WHERE username = ?"

            cursor.execute(query, (username, ))
            data = cursor.fetchone()

            if data:
                return User(*data)

    def get_all(self):
        with DBConnection(self.host) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM users"

            cursor.execute(query)
            data = [
                User(*row)
                for row in cursor.fetchall()
            ]

            return data
