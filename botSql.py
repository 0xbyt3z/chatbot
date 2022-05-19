import sqlite3
import os

database = "database.db"
DDLFile = "sqltables.txt"

def registration(name,age,tel,qual,course):
    id = executeQuery(("select max(id) from clients"))[0][0]
    #make id equals 1 if the table is empty
    id = 1 if id == None else id +1
    executeQuery(f"""insert into clients(id,name,age,tel,qual,course)
     values({id},'{name}','{age}','{tel}','{qual}','{course}')""")
    print(f"\n\nyour registration id is {id}!\nThank you for your interest.")
    return id


def connect():
    con = sqlite3.connect(database)
    return con

def executeQuery(query):
    results = []
    conn = connect()
    #print a successfull connection message if necessary
    cursor = conn.execute(query)
    
    results  = cursor.fetchall()
    conn.commit()
    conn.close()

    return results

def merge():
    #read all the DDL from sqltables and create the tables
    with open(DDLFile,"r") as file:
        query = "".join(file.readlines())
        executeQuery(query)


def printTable(table="clients"):
    results = executeQuery(f"select * from {table}")
    for row in results:
        print(row)
``