# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1,80);
    print("Can you guess my secret?")
    # put your code here
    acertou = False
    t = 0
    while not acertou:
        jogador = int(input("Qual o seu palpite? "))
        t += 1
        if jogador > secret:
            print("Demasiado Alto")
        elif jogador < secret:
            print("Demasiado Baixo")
        else :
            acertou = True
    print("Acertou com",t, "tentativas, Parabéns!")


main()
