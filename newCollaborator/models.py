import sqlite3 as sql

con = sql.connect('database.db')
cursor = con.cursor()

def table_collaborator():
    cursor.execute("""CREATE TABLE collaborator(
            foto BLOB NOT NULL,
            nome VARCHAR(255),
            matricula INT PRIMARY KEY,
            gestor VARCHAR(255), 
            linhas VARCHAR(255), 
            area VAARCHAR(255)
        )"""
    )

def new_collaborator(photo, nameCollab, registration, manager, line, job):
    cursor.execute("""
        INSERT INTO collaborator(foto, nome, matricula, gestor, linhas, area)
        VALUES(?,?,?,?,?,?)""", (photo, nameCollab, registration, manager, line, job)
    )
    con.commit()
    status = 'o Colaborador %s foi cadastrado' % (nameCollab)
    print(status)

try:
    table_collaborator()
except:
    pass