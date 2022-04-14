from lib.grove_moisture_sensor import GroveMoistureSensor
import lib.telegram_send as telegram_send

def send_messages():
    sens = GroveMoistureSensor(2)
    
    reading = sens.moisture    
    if reading >= 101:
        telegram_send.send(messages=[f'All okay! (Water level {reading})'])        
    elif reading in range (20, 101):
        telegram_send.send(messages=[f'Please check me! (Water level {reading})'])        
    else: 
        telegram_send.send(messages=[f'Give me water! (Water level {reading})'])           
        

send_messages()
