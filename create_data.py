# from clean_reading import clean_lines
from sensor_reading import read_data
from water_sensor.message import send_messages


send_messages()
read_data()