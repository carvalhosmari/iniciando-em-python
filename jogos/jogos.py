import adivinhacao
import forca

print("**************************")
print("***** ESCOLHA O JOGO *****")
print("**************************", end="\n\n")

jogo = int(input("Digite o jogo que gostaria de jogar:\n(1) adivinhação (2) forca\n"))

if (jogo == 1):
    adivinhacao.jogar()
elif(jogo == 2):
    forca.jogar()