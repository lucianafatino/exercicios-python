'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    - Se ele ainda vai se alistar ao serviço militar
    - Se é a hora de ele se alistar
    - Se já passou do tempo de alistamento
Seu programa também deve mostrar que falta ou que passou do prazo de alistamento '''
from datetime import date
atual = date.today().year
ano = int(input('Qual é o seu ano de nascimento? '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    anoa = atual + saldo
    print('Ainda faltam {} anos para o seu alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(anoa))
elif idade > 18:
    saldo = idade - 18
    anoa = atual - saldo
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento deveria ter sido em {}.'.format(anoa))