# -*- coding: utf-8 -*-
#Define Libraries
import RPi.GPIO as gpio
# import time

# #Configuring don’t show warnings 
gpio.setwarnings(False)

# #Configuring GPIO
gpio.setmode(gpio.BCM)
gpio.setup(17,gpio.OUT)
gpio.setup(25,gpio.OUT)
gpio.setup(27,gpio.OUT)

# #Configure the pwm objects and initialize its value
pwmBlue = gpio.PWM(25,100)
pwmBlue.start(0)

pwmRed = gpio.PWM(17,100)
pwmRed.start(0)

pwmGreen = gpio.PWM(27,100)
pwmGreen.start(0)
 
#Create the dutycycle variables
dcBlue = 0
dcRed  = 100

#Loop infinite
# def loop_led():
#     while True:
    
#         #increment gradually the luminosity
#         pwmBlue.ChangeDutyCycle(dcBlue)
#         time.sleep(0.001)
#         dcBlue = dcBlue + 1
#         if dcBlue == 100:
#             dcBlue = 0

#         #decrement gradually the luminosity
#         pwmRed.ChangeDutyCycle(dcRed)
#         time.sleep(0.001)
#         dcRed = dcRed - 1
#         if dcRed == 0:
#             dcRed = 100
    
# End code
# gpio.cleanup()
# exit()

def ligaLed():
    print("Ligando o Led")
    pwmGreen.ChangeDutyCycle(100)

def desligaLed():
    print("Desligando o Led")
    pwmGreen.ChangeDutyCycle(0)