from gpiozero import CPUTemperature

def read_temperature():
    cpu = CPUTemperature()    
    temp = round(cpu.temperature, 1)   
    return temp
    
