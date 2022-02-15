'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
'''
from time import sleep
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
opção = 0
while opção != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
    ''')
    opção = int(input('>>>>>> Qual a sua opção? '))
    if opção == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif opção == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('{} é o maior termo.'.format(maior))
    elif opção == 4:
        print('Informe os números novamente.')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    elif opção == 5:
        print('Você optou por sair do programa.')
    else:
        print('Opção inválida, tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa. Volte sempre!')



