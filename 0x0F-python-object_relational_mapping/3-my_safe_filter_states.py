#!/usr/bin/python3

"""This module lists all values in the states table from the database
   hbtn_0e_0_usa where name matches the argument given to the script
   in ascending order and safe from SQL injection using MySQLdb module.
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=argv[1], port=3306,
                              passwd=argv[2], db=argv[3])

    searched_query = argv[4]
    db_cursor = db.cursor()
    query = (
        "SELECT id, name FROM `states` "
        "WHERE name LIKE %s "
        "ORDER BY states.id ASC"
    )
    db_cursor.execute(query, (searched_query,))
    rows = db_cursor.fetchall()

    for row in rows:
        print(row)

    db_cursor.close()
    db.close()
