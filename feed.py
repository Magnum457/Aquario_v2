# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO


# define o pino(BCM) para o servo
servo_pin = 18

#Ajuste estes valores para obter o intervalo completo do movimento do servo
deg_0_pulse   = 0.5 
deg_180_pulse = 2.5
f = 100.0

# Faca alguns calculos dos parametros da largura do pulso
period = 1000/f
k      = 100/period
deg_0_duty = deg_0_pulse*k
pulse_range = deg_180_pulse - deg_0_pulse
duty_range = pulse_range * k
ang = 50

# usa o mapa de portas da placa
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_pin,f)
pwm.start(0)

# calcula o ângulo a ser passado para o servo
def define_angle(angle):
    print("setando o angulo")
    duty = deg_0_duty + (angle/180.0)* duty_range
    print(str(duty))
    pwm.ChangeDutyCycle(round(duty,3))
    
def set_angle(payload):
    if (payload == 0):
        define_angle(47)
        print("angulo de 47")
    elif (payload == 1):
        define_angle(60)
        print("angulo de 60")
    elif (payload == 2):
        define_angle(80)
        print("angulo de 80")
    else:
        print("comando errado")
    # GPIO.cleanup()