'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$ 1000,00
C) Qual é o nome do produto mais barato
'''

totalgasto = prod100 = maisbarato = cont = 0
barato = ''
while True:
    askproduto = str(input('Nome do produto: ')).strip()
    askpreço = float(input('Preço do Produto: R$ '))
    cont += 1
    totalgasto += askpreço
    if askpreço > 1000:
        prod100 += 1
    if cont == 1 or askpreço < maisbarato:
        maisbarato = askpreço
        barato = askproduto
    asksn = ' '
    while asksn not in 'SN':
        asksn = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if asksn == 'N':
        break
print(f'O total gasto foi de R$ {totalgasto:.2f}')
print(f'Temos {prod100} produto custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato}, que custa R$ {maisbarato:.2f}')