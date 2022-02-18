from grove_moisture_sensor import GroveMoistureSensor
import time
import telegram_send

def send_messages():
    sens = GroveMoistureSensor(2)

    while True: 
        reading = sens.moisture    
        if reading >= 101:
            telegram_send.send(messages=[f"Everything's okay! (Water level {reading})"])        
        elif reading in range (20, 101):
            telegram_send.send(messages=[f'Please check me! (Water level {reading})'])        
        else: 
            telegram_send.send(messages=[f'Give me water! (Water level {reading})'])           
        time.sleep(3600)

send_messages()
