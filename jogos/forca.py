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
    print("Parabéns, você acertou :D")

def imprime_derrota(palavra_secreta):
    print(f"Que pena, você perdeu :(. A palavra era {palavra_secreta.upper()}")

def imprime_forca(forca):
    for elemento in forca:
        print(elemento.upper(), end="")

def recebe_tentativa(num_tentativas):
    print(f"\n\nVocê possui {num_tentativas} tentativas.")
    chute = input("\nDigite uma letra: ").lower().strip()

    return chute

def registra_acerto(forca, indice, letra):
    forca[indice] = letra + " "


if(__name__ == "__main__"):
    jogar()