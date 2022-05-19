import sqlite3
import os

database = "database.db"

def connect():
    con = sqlite3.connect(database)
    return con

def executeQuery(query):
    results = [];
    conn = connect()
    #print a successfull connection message if necessary
    cursor = conn.execute(query)
    
    results  = cursor.fetchall()
    conn.commit()
    conn.close()

    return results

def merge():
    #read all the DDL from sqltables and create the tables
    with open("sqltables.txt","r") as file:
        query = "".join(file.readlines())
        executeQuery(query)

if __name__ == "__main__":
    merge()