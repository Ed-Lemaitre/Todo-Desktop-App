from mysql import connector

config = {
    "user": "root",
    "password": "1234",
    "host": "localhost",
    "database": "todo_list_db",
}


def create_connection():
    conn = None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print(f"error connecting to databse: {err}")
    return conn
