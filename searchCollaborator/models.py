import sqlite3 as sql

con = sql.connect('database.db')
cursor = con.cursor()