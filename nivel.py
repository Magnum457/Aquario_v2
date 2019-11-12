# -*- coding: utf-8 -*-
# imports
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
from threading import Thread
# import rele

# Dados
server = "ec2-44-227-11-98.us-west-2.compute.amazonaws.com"
port = "1883"
user = ""
passwd = ""

# configurando os GPIO
def setup():
    GPIO.setmode (GPIO.BCM) # usa o mapa de portas da placa
    bot = 13
    GPIO.setup (bot, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
    estado = 0
    return bot, estado

def loop_nivel():
    try:    
        client = mqtt.Client()
        client.connect(server, port, 60)
        while True:
            bot, estado = setup()
            if GPIO.input(bot)==0:
                    estado = 0
                    print("Cheio")
                    client.publish("aquario/nivel", "cheio")

            elif GPIO.input(bot)==1:
                    estado = 1
                    print("Não Cheio")
                    client.publish("aquario/nivel", "não cheio")
            #         rele.ligaRele()
            # client.publish("aquario/nivel", "cheio")
            time.sleep(1)
                        
    finally:
        print("fechando as GPIOs")
        # GPIO.cleanup()

niv_thread = Thread(target = loop_nivel)