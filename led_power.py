# -*- coding: utf-8 -*-
# import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
from datetime import datetime
import conexao
import led
import bomba
import nivel as niv
import temperatura as temp
import feed

# Dados
server = "44.227.11.98"
port = 1883
user = ""
passwd = ""

# GPIO.setmode (GPIO.BCM) # usa o mapa de portas da placa
# pin_pw = 12
# GPIO.setup (pin_pw, GPIO.OUT)
# pin_con = 5
# GPIO.setup (pin_con, GPIO.OUT) 

# MQTT
## funcoes de callback
def on_connect(client, userdata, flags, rc):
    print("Conectado com resultado: " + str(rc))

    # Tópicos a serem iniciados
    client.subscribe("topico/teste")
    client.publish("start/aquario", "12345")


def on_message(client, userdata, message):
    print("recebendo")
    if(str(message.topic.decode("utf-8")) == "aquario/led/ligar"):
        led.ligaLed()
    elif(str(message.topic.decode("utf-8")) == "aquario/led/desligar"):
        led.desligaLed()
    elif(str(message.topic.decode("utf-8")) == "aquario/bomba/ligar"):
        bomba.ligaBomba()
    elif(str(message.topic.decode("utf-8")) == "aquario/bomba/desligar"):
        bomba.desligaBomba()
    elif(str(message.topic.decode("utf-8")) == "aquario/feed/aberto"):
        print("alimenta")
        feed.set_angle(2)
    elif(str(message.topic.decode("utf-8")) == "aquario/feed/meio"):
        print("alimentb")
        feed.set_angle(1)
    elif(str(message.topic.decode("utf-8")) == "aquario/feed/fechado"):
        print("alimentc")
        feed.set_angle(0)
#       if (str(message.payload.decode("utf-8")) == "ligar"):
#           led.ligaLed()
#       elif(str(message.payload.decode("utf-8")) == "desligar"):
#           led.desligaLed()


def liga_conexao():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("44.227.11.98", 1883, 60)
    client.subscribe("aquario/led/ligar")
    client.subscribe("aquario/led/desligar")
    client.subscribe("aquario/bomba/ligar")
    client.subscribe("aquario/bomba/desligar")
    client.subscribe("aquario/feed/aberto")
    client.subscribe("aquario/feed/meio")
    client.subscribe("aquario/feed/fechado")
    
    temp.temp_thread.start()
    niv.niv_thread.start()
    
    client.loop_forever()