# -*- coding: utf-8 -*-
# imports
import botao

# Simulação do botão
while True:
    start_input = input("Digite o seu comando: ")
    if(start_input == "exit"):
        break
    elif(start_input == "start"):
        botao.botao_thread.start()
        break
    else:
        print("comando inválido")

