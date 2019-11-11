# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import temperatura as temp
from threading import Thread
import nivel as niv
import feed
import led

# Dados
server = "ec2-44-227-11-98.us-west-2.compute.amazonaws.com"
port = "1883"
user = ""
passwd = ""

# Topicos
temperatura_topico = "aquario/temperatura"
nivel_topico = "aquario/nivel"
start_topico = "aquario/start"
led_topico = "aquario/led"
racao_topico = "aquario/racao"

# MQTT
## funcoes de callback
def on_connect(client, userdata, flags, rc):
    print("Conectado com resultado: " + str(rc))

    # Tópicos a serem iniciados
    client.subscribe(led_topico)
    client.subscribe(racao_topico)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if(msg.topic == led_topico):
        print("chamada na função led")
        if(str(msg.payload) == "ligar"):
            led.ligaLed()
        elif(str(msg.payload) == "desligar"):
            led.desligaLed()
        else:
            print("comando inválido!")
    elif(msg.topic == racao_topico):
        print("chamada na função alimentação")
        feed.set_angle(str(msg.payload))
    else:
        print("comando inválido!")

# ## instancia do cliente
def conecta():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(server, port, 60)

    temp.temp_thread.start()
    niv.niv_thread.start()

    client.loop_forever()

conecta_thread = Thread(target = conecta)