from grove_moisture_sensor import GroveMoistureSensor
sens = GroveMoistureSensor(2)

readings = {'Water_level': ''}
reading = sens.moisture  
reading = str(reading)
readings['Water_level'] = reading
print (readings)