import sqlite3
from sqlite3 import Error
from grove_moisture_sensor import GroveMoistureSensor

def create_connection(db_file):
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)        
    except Error as e:
        print(e)
    return conn 
    # finally:
        # if conn:
            # conn.close()

def add_reading(conn, reading):
    sql = ''' INSERT INTO readings(level)
              VALUES(?) '''    
    cur = conn.cursor()   
    cur.execute(sql, reading)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"/home/pi/Documents/tests/water_sensor/readings.db"
    conn = create_connection(database)    
    with conn:     
        sens = GroveMoistureSensor(2)
        reading = sens.moisture       
        add_reading(conn, (reading,))

if __name__ == '__main__':
    main()

