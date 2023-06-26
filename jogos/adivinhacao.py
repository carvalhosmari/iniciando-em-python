import random

def jogar():
    print("*************************")
    print("** JOGO DE ADIVINHAÇÃO **")
    print("*************************", end="\n\n")

    numero_secreto = random.randint(1, 101)
    max_tentativas = 0
    rodada = 1
    pontuacao = 1000

    nivel = int(input("Digite o nível de dificuldade do jogo:\n(1) fácil (2) médio (3) difícil\n"))

    if(nivel == 1):
        max_tentativas = 10
    elif(nivel == 2):
        max_tentativas = 7
    elif(nivel == 3):
        max_tentativas = 3

    #utilizando loop while
    while(rodada <= max_tentativas):
        print("Tentativa {} de {}:".format(rodada, max_tentativas))

        palpite = int(input("Digite um numero: "))

        if(numero_secreto == palpite):
            print(f"Você acertou!\n")
            pontuacao += 300
            break
        elif(numero_secreto > palpite):
            print("Você errou! O numero secreto é maior do que seu palpite.\n")
            pontuacao -= abs(palpite - numero_secreto)
        else:
            print("Você errou! O numero secreto é menor do que seu palpite.\n")
            pontuacao -= abs(palpite - numero_secreto)

        rodada+= 1

    print(f"Fim de jogo! O numero secreto é {numero_secreto}. Sua pontuação final é {pontuacao}")

if(__name__ == "__main__"):
    jogar()