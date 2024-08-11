import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    limpar_tela()
    OsJogos = ["Jogo Da Forca", "Jogo Da Velha", "Pedra, Papel e Tesoura"]
    for x, y in enumerate(OsJogos):
        print(f"{x + 1}: {y}")
    print("\n")

    try:
        Resposta = int(input("Digite o número que corresponde ao jogo que deseja entrar: "))

        if Resposta == 1:

            limpar_tela()
            from Jogos import JogoDaForca
            JogoDaForca.jogo()

        elif Resposta == 2:

            limpar_tela()
            from Jogos import JogoDaVelha
            JogoDaVelha.jogo()

        elif Resposta == 3:

            limpar_tela()
            from Jogos import PedraPapelTesoura
            PedraPapelTesoura.jogo()
            
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")