# -*- coding: utf-8 -*-
# import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
from datetime import datetime
import conexao

# Dados
server = "ec2-44-227-11-98.us-west-2.compute.amazonaws.com"
port = "1883"
user = ""
passwd = ""

# GPIO.setmode (GPIO.BCM) # usa o mapa de portas da placa
# pin_pw = 12
# GPIO.setup (pin_pw, GPIO.OUT)
# pin_con = 5
# GPIO.setup (pin_con, GPIO.OUT) 

def blink():
    for i in range(5):
        print("\nliga Led\n")
        time.sleep(1)
        print("\ndeliga Led\n")
        time.sleep(1)
        print("\nliga led\n")
        time.sleep(1)
        print("\ndesliga led\n")

# Retorna o identificador do aquario
def getAquarioId():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
    except:
    cpuserial = "ERROR000000000"


    return "SmartAquario#"+str(cpuserial)

# MQTT
## funcoes de callback
def on_connect(client, userdata, flags, rc):
    print("Conectado com resultado: " + str(rc))

    # Tópicos a serem iniciados
    client.publish("start/aquario", "12345")
    client.subscribe("start/app")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if(msg.topic == "start/app"):
        cadastro_app = str(msg.payload)
        conexao.conecta_thread.start()


def liga_conexao():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(server, port, 60)

    client.loop_start()
    now = datetime.now().second
    print(type(now))
    blink()

    if (datetime.now().second > now + 30):
        client.loop_end()
        