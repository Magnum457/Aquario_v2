# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import temperatura as temp
from threading import Thread
import nivel as niv
import feed
import led
import bomba

# Dados
server = "44.227.11.98"
port = 1883
user = ""
passwd = ""

# Topicos
temperatura_topico = "aquario/temperatura"
nivel_topico = "aquario/nivel"
start_topico = "aquario/start"
led_topico = "aquario/led"
racao_topico = "aquario/racao"
bomba_topico = "aquario/bomba"

# MQTT
## funcoes de callback
def on_connect(client, userdata, flags, rc):
    print("Conectado com resultado: " + str(rc))
    print("deu certo")

    # Tópicos a serem iniciados
    client.subscribe(led_topico)
    client.subscribe(racao_topico)
    client.subscribe(bomba_topico)

def on_message(client, userdata, msg):
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
    elif(msg.topic == bomba_topico):
        print("chamada na função da bomba")
        if(str(msg.payload) == "ligar"):
            bomba.ligaBomba()
        elif(str(msg.payload) == "desligar"):
            bomba.desligaBomba()
        else:
            print("comando inválido!")
    else:
        print("comando inválido!")

# ## instancia do cliente
def conecta():
    print("cheguei até aqui")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("44.227.11.98", 1883, 60)
    
    client.subscribe(led_topico)
    client.subscribe(racao_topico)
    client.subscribe(bomba_topico)

    temp.temp_thread.start()
    niv.niv_thread.start()

    client.loop_forever()

conecta_thread = Thread(target = conecta)