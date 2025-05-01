from random import randint
from time import sleep

titulo = 'JOGO DE ADIVINHAÇÃO'
print('\033[0;34m~=~\033[m' * 20)
print('\033[1;31m{:^58}'.format(titulo))
print('\033[0;34m~=~' * 20)

# Jogador pensar em um número
jogador = int(input('\033[;30mDigite um número de 1 a 5 para começar o jogo: '))
print('\033[1;34mCarregando...')
sleep(3)
# Faz o computador pensar em um número
computador = randint(1, 5)

if jogador == computador:
    print(f'\033[1;32mVOCÊ GANHOU! o número corretor é {computador}\033[m')
else:
    print(f'\033[1;31mVOCÊ PERDEU! o número corretor é {computador}\033[m')
