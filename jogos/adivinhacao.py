import random

print("*************************")
print("Jogo de adivinhação")
print("*************************", end="\n\n")

numero_secreto = random.randint(1, 101)
max_tentativas = 3
rodada = 1

#utilizando loop while
while(rodada <= max_tentativas):
    print("Tentativa {} de {}:".format(rodada, max_tentativas))

    palpite = int(input("Digite um numero: "))

    if(numero_secreto == palpite):
        print("Você acertou!\n")
        break
    elif(numero_secreto > palpite):
        print("Você errou! O numero secreto é maior do que seu palpite.\n")
    else:
        print("Você errou! O numero secreto é menor do que seu palpite.\n")

    rodada+= 1

print(f"Fim de jogo! O número que deveria ser adivinhado era {numero_secreto}")

