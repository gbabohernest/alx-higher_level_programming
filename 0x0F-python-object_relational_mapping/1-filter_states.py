#!/usr/bin/python3

"""This module lists all states with a name starting with N
   from the database hbtn_0e_0_usa in ascending order using
   MySQLdb module.
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=argv[1], port=3306,
                              passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()
    db_cursor.execute(
        "SELECT id, name FROM `states` "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY states.id ASC"
    )
    rows = db_cursor.fetchall()

    for row in rows:
        print(row)

    db_cursor.close()
    db.close()
