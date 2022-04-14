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

# creating tables in db if none exist before
def main():
    database = r"/home/pi/Documents/tests/water_sensor/readings.db"

    sql_create_levels_table = """ CREATE TABLE IF NOT EXISTS readings (
                                        id integer PRIMARY KEY,
                                        date text,
                                        level integer NOT NULL,    
                                        temp real                   
                                    ); """

   
    conn = create_connection(database)

   
    if conn is not None:        
        create_table(conn, sql_create_levels_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()