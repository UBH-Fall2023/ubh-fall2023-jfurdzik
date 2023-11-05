import sqlite3
from sre_constants import IN

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO entries (content) VALUES ('content goes here')")
cur.execute("INSERT INTO entries (content) VALUES ('more content goes here')")

connection.commit()
connection.close()