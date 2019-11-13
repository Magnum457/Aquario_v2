# import
from threading import Thread
import os
import glob
import time
import paho.mqtt.client as mqtt
from random import randint
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Dados
server = "44.227.11.98"
port = 1883
user = ""
passwd = ""
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
    
def loop_temp():
    while True:
        temp_c, temp_f = read_temp()
        #print(temp_c)
        #temp_c = randint(20,30)
        client = mqtt.Client()
        client.connect(server, port, 60)
        client.publish("aquario/temperatura", temp_c)
        time.sleep(10)

temp_thread = Thread(target = loop_temp)