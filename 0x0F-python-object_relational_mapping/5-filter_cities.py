#!/usr/bin/python3

"""This module takes in the name of a state as argument and
   lists all cities from that state, using the database hbtn_0e_4_usa
   in ascending order using MySQLdb module.
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=argv[1], port=3306,
                              passwd=argv[2], db=argv[3])

    state_name = argv[4]

    db_cursor = db.cursor()
    query = ("SELECT cities.name "
             "FROM cities "
             "INNER JOIN states "
             "ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")

    db_cursor.execute(query, (state_name,))

    rows = db_cursor.fetchall()

    cities = ', '.join(row[0] for row in rows)
    print(cities)

    db_cursor.close()
    db.close()
