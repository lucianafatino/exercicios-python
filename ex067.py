'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for um número negativo.
'''
while True:
    print('-' * 40)
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if tab < 0:
        break
    for c in range(1,11):
        print(f'{c} x {tab} = {c*tab}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')