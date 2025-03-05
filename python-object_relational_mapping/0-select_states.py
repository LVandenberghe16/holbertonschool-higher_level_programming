#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
