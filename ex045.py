'''Crie um programa que faça o computador jogar jokenpô com você'''
from random import randint
from time import sleep

print('Vamos jogar jokenpô!')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções são:
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('-=' * 15)
print('A jogada do computador foi: {}'.format(itens[computador]))
print('A sua jogada foi: {}'.format(itens[jogador]))
print('-=' * 15)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('GANHOU!!')
    elif jogador == 2:
        print('PERDEU!')
    else:
        print('[ERRO] JOGADA INVÁLIDA')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('GANHOU!!')
    else:
        print('[ERRO] JOGADA INVÁLIDA')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('GANHOU!!')
    elif jogador == 1:
        print('PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('[ERRO] JOGADA INVÁLIDA')
