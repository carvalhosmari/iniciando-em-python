import random

def jogar():

    acertos = 0
    max_tentativas = 6
    acertou = False
    excedeu = False

    imprime_abertura()

    palavra = seleciona_palavra()
    forca = retorna_forca(palavra)

    while(not acertou and not excedeu):
        imprime_forca(forca)

        tentativa = recebe_tentativa(max_tentativas)

        if(palavra.count(tentativa) > 0):
            for index, elem in enumerate(palavra):
                if(tentativa == elem):
                    registra_acerto(forca, index, elem)
                    acertos += 1
        else:
            max_tentativas -= 1

        desenha_forca(max_tentativas)

        if (acertos >= len(palavra)):
            acertou = True
            imprime_vitoria()
        elif(max_tentativas == 0):
            excedeu = True
            imprime_derrota(palavra)

def imprime_abertura():
    print("*************************")
    print("***** JOGO DE FORCA *****")
    print("*************************", end="\n\n")

def seleciona_palavra():
    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha)

    indice_palavra = random.randrange(0, len(palavras))
    palavra = palavras[indice_palavra].strip()

    return palavra

def retorna_forca(palavra_secreta):
    forca = ["_ " for letra in palavra_secreta]

    return forca

def imprime_vitoria():
    print(" Parabéns, você ganhou! ")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta.upper()))
    print("    _______________        ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\   ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/    ")
    print(" |   XXX       XXX   |     ")
    print(" |                   |     ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |       ")
    print("   | I I I I I I I |       ")
    print("   |  I I I I I I  |       ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_forca(forca):
    for elemento in forca:
        print(elemento.upper(), end="")

def recebe_tentativa(num_tentativas):
    print(f"\n\nVocê possui {num_tentativas} tentativas.")
    chute = input("\nDigite uma letra: ").lower().strip()

    return chute

def registra_acerto(forca, indice, letra):
    forca[indice] = letra + " "

def desenha_forca(max_tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if (max_tentativas == 5):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (max_tentativas == 4):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if (max_tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |            ")

    if (max_tentativas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (max_tentativas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (max_tentativas == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()