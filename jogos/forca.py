def jogar():
    print("*************************")
    print("***** JOGO DE FORCA *****")
    print("*************************", end="\n\n")

    acertos = 0
    max_tentativas = 6
    palavra = "paralelepipedo"
    forca = []
    acertou = False
    excedeu = False

    for caracter in range(0, len(palavra)):
        forca.append("_ ")

    while(not acertou and not excedeu):
        for elemento in forca:
            print(elemento.upper(), end="")

        print(f"\n\nVocê possui {max_tentativas} tentativas.")

        tentativa = input("\nDigite uma letra: ").lower().strip()

        if(palavra.count(tentativa) != 0):
            for index, elem in enumerate(palavra):
                if(tentativa == elem):
                    forca[index] = elem + " "
                    acertos += 1
            if(acertos >= len(palavra)):
                acertou = True
                print("\nParabens! Você ganhou!!!")
        else:
            max_tentativas -= 1

            if(max_tentativas == 0):
                excedeu = True
                print(f"\nPerdeu otarioooooo! A palavra era: {palavra}")

if(__name__ == "__main__"):
    jogar()