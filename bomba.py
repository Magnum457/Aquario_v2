import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

pin = 7

GPIO.setup(pin,GPIO.OUT)

try:
    def ligaBomba():
        print("Ligando o rele")
        GPIO.output(pin,1)

    def desligaBomba():
        print("Desligando o rele")
        GPIO.output(pin,0) 
        
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()


