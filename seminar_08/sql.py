import sqlite3


def record_add(name, contact_group, phone, phone_type):
    sqlite_connection = sqlite3.connect('phonebook.db')
    cursor = sqlite_connection.cursor()
    query = f"""INSERT INTO people(name, id_group) 
                VALUES("{name}",{contact_group})"""
    cursor.execute(query)
    row_id = cursor.lastrowid
    query = f"""INSERT INTO phones (id_people,phone,id_phonetype)
                VALUES({row_id},{phone},{phone_type})"""

    cursor.execute(query)
    sqlite_connection.commit()
    sqlite_connection.close()


def record_del(id_people):
    sqlite_connection = sqlite3.connect('phonebook.db')
    cursor = sqlite_connection.cursor()
    query = "PRAGMA foreign_keys = ON;"
    cursor.execute(query)
    query = f"""DELETE FROM people WHERE id_people = "{id_people}" """
    cursor.execute(query)
    sqlite_connection.commit()
    sqlite_connection.close()


def record_find(data):
    sqlite_connection = sqlite3.connect('phonebook.db')
    cursor = sqlite_connection.cursor()
    query = f"""SELECT P.id_people, P.name, PH.phone, PT.name, G.name
                FROM people AS P
                JOIN phones AS PH ON P.id_people = PH.id_people
                JOIN phone_types AS PT ON PH.id_phonetype = PT.id_phonetype
                JOIN groups AS G ON P.id_group = G.id_group
                WHERE P.name LIKE "%{data}%"
                OR P.name LIKE "%{data.capitalize()}%"
                OR PH.phone LIKE "%{data}%" 
                ORDER BY P.name"""
    cursor.execute(query)
    records = cursor.fetchall()
    sqlite_connection.close()
    return records


def change_name(data, id_people):
    sqlite_connection = sqlite3.connect('phonebook.db')
    cursor = sqlite_connection.cursor()
    query = f"""UPDATE people SET name="{data}" WHERE id_people="{id_people}" """
    cursor.execute(query)
    sqlite_connection.commit()
    sqlite_connection.close()


def add_phone(id_people, phone, id_phonetype):
    sqlite_connection = sqlite3.connect('phonebook.db')
    cursor = sqlite_connection.cursor()
    query = f"""INSERT INTO phones (id_people,phone,id_phonetype) 
                VALUES ({id_people},{phone},{id_phonetype}) """
    cursor.execute(query)
    sqlite_connection.commit()
    sqlite_connection.close()

def del_phone(id_people, phone):
    sqlite_connection = sqlite3.connect('phonebook.db')
    cursor = sqlite_connection.cursor()
    query = f"""DELETE FROM phones
                WHERE id_people='{id_people}' AND phone='{phone}' """
    cursor.execute(query)
    sqlite_connection.commit()
    sqlite_connection.close()
