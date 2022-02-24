# create one table, name: 'readings'
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"/home/pi/Documents/tests/water_sensor/readings.db"

    sql_create_levels_table = """ CREATE TABLE IF NOT EXISTS readings (
                                        id integer PRIMARY KEY,
                                        date text,
                                        level integer NOT NULL,    
                                        temp real                   
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_levels_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()