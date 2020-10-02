import sqlite3 as sql

con = sql.connect('database.db')
cursor = con.cursor()


def table_line():
    cursor.execute("""CREATE TABLE line(
            nome VARCHAR(30), 
            abrev VARCHAR(8) PRIMARY KEY,
            tipo VARVCAR(20)       
        )"""
    )


def new_line(nameLine, abbreviation, typeLine):
    cursor.execute("""
    INSERT INTO line(nome, abrev, tipo)
    VALUES(?,?,?)""", (nameLine, abbreviation, typeLine))
    status = 'Linha inserida'
    con.commit()
    return status

try:
    table_line()
except:
    pass