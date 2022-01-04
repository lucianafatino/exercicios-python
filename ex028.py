# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu

#Minha resolução
from random import randint
from time import sleep
n = randint(0,5) # Faz o computador 'pensar'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
nu = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if nu == n:
    print('Você ganhou! Eu pensei no número {}'.format(n))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(n, nu))

