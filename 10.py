lista_jogadores = ["Alexandre", "Bernardo", "Diogo", "Daniel" "Eduardo"]

while True:
    print("\n Gestão da equipa sharkcooders")
    print(" 1 Ver a equipa atual")
    print(" 2 substituir um jogador")
    print(" 3 adicionar um novo jogador ")
    print(" 4 remover um jogador")
    print(" 5 reorganizar a equipa")
    print(" 6 sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
       print("\n equipa qtual:")
       for i, jogador in enumerate (lista_jogadores):
        print(f'{i} - {jogador}')

    elif escolha == 2:
        print("\n Equipa atual:")
        for i, jogador in enumerate(lista_jogadores):
            print(f"{i} - {jogador}")
        posicao = int(input("insire o número do jogador a substituir: "))
        if 0 <= posicao < len(lista_jogadores):
            novo_jogador = int(input("insira o jogador"))
            novo_jogador[posicao] = novo_jogador
            lista_jogadores[posicao] = novo_jogador


    if escolha == 6:
        print(" A gestão da equipe foi encerrada. até a proxima.")
    break

else:
        print("opção invalida")
