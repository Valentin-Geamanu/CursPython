"""
Ineteractiunea cu tabelul users
"""

# CRUD OPERATIONS
# CREATE
# READ
# UPDATE
# DELETE

import sqlite3

connection = sqlite3.connect('marcketplace.db')
cursor = connection.cursor

# CREATE USER

# user 1

# are completate doar campurile obligatorii

cursor.execute(

    """
    INSERT INTO users (username, email, password, first_name, last_name)
    VALUES ('cosminabacter01', 'cosmina@yahoo.ro', 'cosmina123', 'Cosmina', 'Bacter');
    """
)
connection.commit()

# user 2

user_query = """
INSERT INTO users(username, email, password, first_name, last_name)
VALUES (?, ?, ?, ?, ?, ?

"""