'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idadde:
    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 19 anos: JUNIOR
    - Até 25 anos: SÊNIOR
    - Acima: MASTER
'''
from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM.')
elif idade <= 14:
    print('Categoria: INFANTIL.')
elif idade <= 19:
    print('Categoria: JUNIOR.')
elif idade <= 25:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')