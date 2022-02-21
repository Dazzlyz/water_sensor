from grove_moisture_sensor import GroveMoistureSensor
sens = GroveMoistureSensor(2)

readings = {'Water_level': ''}
reading = sens.moisture  

sens = GroveMoistureSensor(2)
reading = sens.moisture       
print((reading,))
