# -*- coding: utf-8 -*-
# imports
import botao
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led_pwr = 12
btn_input = 6
GPIO.setup(led_pwr,GPIO.OUT)
GPIO.setup(btn_input,GPIO.IN)
GPIO.output(led_pwr,1)

# Simulação do botão
while True:
    start_input = input("Digite o seu comando: ")
    if(start_input == "exit"):
        GPIO.output(botao, 0)
        break
    elif(start_input == "start"):
        botao.botao_thread.start()
        break
    else:
        print("comando inválido")

