import sqlite3
from sqlite3 import Error
from lib.grove_moisture_sensor import GroveMoistureSensor
from temp import read_temperature
from date import get_date

# code to add data to database, updates every 10 minutes via command line tool (cron)

def create_connection(db_file):    
    conn = None
    try:
        conn = sqlite3.connect(db_file)        
    except Error as e:
        print(e)
    return conn 

# adding data to correct tables
def add_reading(conn, reading):
    sql = ''' INSERT INTO readings(date, level, temp)
              VALUES(?,?,?) '''    
    cur = conn.cursor()   
    cur.execute(sql, reading)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"/home/pi/Documents/tests/water_sensor/readings.db"
    conn = create_connection(database)    
    with conn:     
        sens = GroveMoistureSensor(2)
        date = get_date()        
        temp = read_temperature()
        temp = str(temp)
        moisture = sens.moisture
        reading = (date, moisture, temp)
        
        add_reading(conn, reading)

if __name__ == '__main__':
    main()

