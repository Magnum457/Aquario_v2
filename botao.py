# -*- coding: utf-8 -*-
# import RPi.GPIO as GPIO
import time
from threading import Thread
import conexao
import paho.mqtt.client as mqtt
import led_power

# GPIO.setmode (GPIO.BCM) # usa o mapa de portas da placa
# pin_con = 5
# GPIO.setup (pin_con, GPIO.OUT) 

# função a ser chamada ao apertar o botão
def ligar_aquario():
    print("blink de 30 segundos")
    botao = 1
    # for i in range(10):
            # time.sleep(1)
            # GPIO.output(pin_con,1)
            # time.sleep(1)
            # GPIO.output(pin_con,0) 
            # time.sleep(1)
    while botao != 0:
        # if(conexao.conecta_thread.is_alive() != True):

        #     conexao.conecta_thread.start()
        led_power.liga_conexao()
        # if(res != ""):
        #    print(res)
        text = input("Para desligar digite (exit): ")
        if (text == "exit"):
            desligar_aquario()
            botao = 0
        

def desligar_aquario():
    if(conexao.conecta_thread.is_alive()):
        conexao.conecta_thread.join(2.0)
    exit()

#End code
# GPIO.cleanup()
# exit()

botao_thread = Thread(target = ligar_aquario)