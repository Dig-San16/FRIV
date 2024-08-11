import pygame 
import os

def jogo():

    def musica(som):
        pygame.mixer.init()
        pygame.mixer.music.load(som)
        pygame.mixer.music.play(-1)

    def limpar_tela():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def Joguinho(Joga):

        musica('kahoot.mp3')

        tabela = {
                "1": " ", "2": " ", "3": " ",
                    
                "4": " ", "5": " ", "6": " ",

                "7": " ", "8": " ", "9": " "
        }

        jogador = Joga
        jogadas = []
        venceu = False

        vencedor = [
            # Linhas
            ["1", "2", "3"], 
            ["4", "5", "6"], 
            ["7", "8", "9"], 

            # Colunas
            ["1", "4", "7"], 
            ["2", "5", "8"], 
            ["3", "6", "9"],

            # Diagonais
            ["1", "5", "9"], 
            ["3", "5", "7"] 
        ]

        def tabuleiro():
            print("\n")
            print("         |         |")
            print(f"    {tabela['1']}    |    {tabela['2']}    |    {tabela['3']}")
            print("         |         |")
            print("---------+---------+---------")
            print("         |         |")
            print(f"    {tabela['4']}    |    {tabela['5']}    |    {tabela['6']}")
            print("         |         |")
            print("---------+---------+---------")
            print("         |         |")
            print(f"    {tabela['7']}    |    {tabela['8']}    |    {tabela['9']}")
            print("         |         |")

        while True:
        
            tabuleiro()

            if len(jogadas) == 9:
                print('\n')
                print("\033[1;33;40mEMPATE?\033[m")
                musica("flautabugada.mp3")
                break

            print("\n")
            posição = input(f"jogador {jogador}, escolha a posição: ")
            print("\n")

            if posição in jogadas:
                print("\033[1;33;40messe espaço ja foi usado\033[m")
                continue

            if posição in tabela:
                tabela[posição] = jogador
                jogadas += posição
            else:
                print("\033[1;33;40mDigite entre 1 ou 9 pls\033[m")
                print("\n")
                continue

            for linha in vencedor:
                if tabela[linha[0]] == tabela[linha[1]] == tabela[linha[2]] != " ":
                    venceu = True

            if venceu:
                tabuleiro()
                print('\n')
                print(f"\033[1;32;40mJogador {jogador} venceu!\033[m") 
                musica('victory.mp3')
                break   

            jogador = "O" if jogador == "X" else "X"
            
        while True:
            print("\n")
            a = input("Deseja jogar novamente? (S/N): ").lower().strip()
            if a == "s":
                limpar_tela()
                print("/" * 30)
                print("\033[0;33;40m        JOGO DA VELHA       \033[m")
                print("/" * 30)
                Joguinho(Marca)
            
            elif a == "n":
                exit()
            else:
                print("\033[1;31;40mDigite entre S ou N pls\033[m")

    while True:
        print("/" * 30)
        print("\033[0;33;40m        JOGO DA VELHA       \033[m")
        print("/" * 30)
        print("\n")
        Marca = input("Digite entre X ou O: ").upper().strip()
        if Marca != 'X' and Marca != 'O':
            print("Digite direito isso ai mano")
        else:
            Joguinho(Marca)
