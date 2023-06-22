print("*************************")
print("Jogo de adivinhação")
print("*************************", end="\n\n")

numero_secreto = 34
max_tentativas = 3
rodada = 1

#utilizando loop while
'''
while(rodada <= max_tentativas):
    print("\nTentativa {} de {}:".format(rodada, max_tentativas))

    palpite = int(input("Digite um numero: "))

    if(numero_secreto == palpite):
        print("Você acertou!")
        break
    elif(numero_secreto > palpite):
        print("Você errou! O numero secreto é maior do que seu palpite.")
    else:
        print("Você errou! O numero secreto é menor do que seu palpite.")

    rodada+= 1

print("Fim de jogo!") '''

#utilizando loop for
for tentativa in range(rodada, max_tentativas + 1, 1):
    print("\nTentativa {} de {}:".format(tentativa, max_tentativas))

    palpite = int(input("Digite um numero: "))

    if (numero_secreto == palpite):
        print("Você acertou!")
        break
    elif (numero_secreto > palpite):
        print("Você errou! O numero secreto é maior do que seu palpite.")
    else:
        print("Você errou! O numero secreto é menor do que seu palpite.")

print("Fim de jogo!")