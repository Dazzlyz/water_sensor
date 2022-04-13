from lib.grove_moisture_sensor import GroveMoistureSensor
import time

def read_data():
    sens = GroveMoistureSensor(2)
    while True: 
        reading = sens.moisture  
        with open('sensor.txt', 'a') as file:
            file.write(f'{reading}\n')
        time.sleep(600)

read_data()