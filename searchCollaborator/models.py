import sqlite3 as sql

con = sql.connect('database.db')
cursor = con.cursor()

def query_collaborator(query):
    cursor.execute("""
        SELECT * FROM collaborator 
        %s""" % (query))
    results = cursor.fetchall()
    return results