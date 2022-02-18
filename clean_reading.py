from os import remove
import readline

def clean_lines():
    lines = []

    with open('sensor.txt', 'r') as file:
        lines = file.readlines()

    if len(lines) >= 100:
        with open('sensor.txt', 'r+') as file:
            file.seek(0)
            file.truncate()
            file.writelines(lines[50:])
                
                   

