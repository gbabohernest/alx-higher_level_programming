#!/usr/bin/python3

"""This module lists all cities from the database
   hbtn_0e_0_usa in ascending order using MySQLdb module.
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=argv[1], port=3306,
                              passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()
    query = "SELECT id, name FROM cities ORDER BY cities.id ASC"
    db_cursor.execute(query)

    rows = db_cursor.fetchall()

    for row in rows:
        print(row)

    db_cursor.close()
    db.close()
