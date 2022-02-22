from mysql import connector

from database.connector import create_connection


def insert(data):
    conn = create_connection()
    sql = """ INSERT INTO todo (descripcion_tarea, estado) VALUES (%s, %s)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error inserting data: {err}")
        return False
    finally:
        cur.close()
        conn.close()


def delete(data):
    conn = create_connection()
    sql = """ DELETE"""
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error deleting data: {err}")
        return False
    finally:
        cur.close()
        conn.close()
