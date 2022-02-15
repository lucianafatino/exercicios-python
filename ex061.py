'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os
10 primeiros termos da progressão usando a estrutura while
'''
print('=' * 30)
print('10 TERMOS DE UMA PA'.center(30))
print('=' * 30)

inicio = int(input('Primeiro termo: '))
passo = int(input('Razão da PA: '))
termos = inicio
cont = 1
print('A PA será: ')
while cont <= 10:
    print('{} ↠ '.format(termos), end="")
    termos += passo
    cont += 1
print('ACABOU')