#Importando bibliotecas
from time import sleep
import random
import os

def jogo():

    def limpar_tela():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    #Função enche linguiça

    def maquina(falar):
        sleep(0.3)
        print('\n')
        print(falar)
        print('\n')

    #Definindo uma lista

    escolha = ["Pedra", "Papel", "Tesoura"]

    while True:

        print("/" * 30)
        print("\033[0;33;40m    PEDRA, PAPEL e TESOURA       \033[m")
        print("/" * 30)
        print("\n")

        for p, e in enumerate(escolha):
            print(f"{p + 1}: {e}")
            
        try:
            resposta = int(input("\ndigite um numero das três opções acima: "))
            if resposta < 1 or resposta > 3:
                print("\033[0;31;40mOpção inválida, por favor escreva entre 1 a 3\033[m")
                
            #Pegando a opção escolhida da resposta pela lista

            Pc = escolha[resposta - 1]

            #Computador faz a sua escolha

            b = random.choice(escolha)

            print("Prontos?")
            sleep(0.9)
            maquina("JO")
            maquina("KEN")
            sleep(0)
            maquina("PO!")

            #Exibindo as escolhas dos jogadores

            print(f"Computador: \033[0;36;40m{b}\033[m")
            print(f"Jogador: \033[0;36;40m{Pc}\033[m")
            sleep(2)

            #Funcionamento da escolha do vencedor

            if Pc == b:
                print("\033[0;33;40mEMPATE!\033[m")
                sleep(2)
                limpar_tela()
            elif (Pc == "Papel" and b == "Tesoura") or (Pc == "Tesoura" and b == "Pedra") or (Pc == "Pedra" and b == "Papel"):
                print("\033[0;31;40mO computador vence!\033[m")
                sleep(2)
                limpar_tela()
            else:
                print("\033[0;32;40mO jogador vence!\033[m")
                sleep(2)
                limpar_tela()

        except ValueError:
            print("\033[0;31;40mOpção inválida, por favor escreva entre 1 a 3\033[m")
