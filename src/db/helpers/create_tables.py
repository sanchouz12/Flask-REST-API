from .connection import DBConnection


def create_table(host):
    if host == "users":
        host = "databases/" + host + ".db"

        with DBConnection(host) as connection:
            cursor = connection.cursor()
            query = "CREATE TABLE IF NOT EXISTS users (id integer primary key, username text, password text)"

            cursor.execute(query)
    elif host == "items":
        host = "databases/" + host + ".db"

        with DBConnection(host) as connection:
            cursor = connection.cursor()
            query = "CREATE TABLE IF NOT EXISTS items (id integer primary key, name text, price int, description text)"

            cursor.execute(query)

    return host
