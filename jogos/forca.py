def jogar():
    print("*************************")
    print("***** JOGO DE FORCA *****")
    print("*************************", end="\n\n")

    acertos = 0
    max_tentativas = 6
    palavra = "exemplo"
    forca = []
    acertou = False
    excedeu = False

    for letra in palavra:
        forca.append("_ ")

    while(not acertou and not excedeu):
        for elemento in forca:
            print(elemento, end="")

        print(f"\nVocê possui {max_tentativas} tentativas. {acertos}\n")

        tentativa = input("\nDigite uma letra: ").lower()

        if(palavra.count(tentativa) != 0):
            for index, elem in enumerate(palavra):
                if(tentativa == elem):
                    forca[index] = elem + " "
                    acertos += 1
            if(acertos >= len(palavra)):
                acertou = True
                print("Parabens! Você ganhou!!!")
        else:
            max_tentativas -= 1

            if(max_tentativas == 0):
                excedeu = True
                print("Perdeu otarioooooo!")

if(__name__ == "__main__"):
    jogar()