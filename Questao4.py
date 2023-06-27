import random

palpite = -1
numero_sorteado = random.randint(1, 50) 

while palpite != numero_sorteado:
    palpite = int(input('Digite um palpite: '))

    if palpite < numero_sorteado:
        print('Palpite muito baixo. Tente novamente.')
    elif palpite > numero_sorteado:
        print('Palpite muito alto. Tente novamente.')
    else:
        print('Parabéns! Você acertou.')


