from lib.grove_moisture_sensor import GroveMoistureSensor

sens = GroveMoistureSensor(2)
reading = sens.moisture  
print (reading)

