'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
a condição de pagamento:
    - À vista dinheiro/cheque: 10% de desconto
    - À vista no cartão: 5% de desconto
    - Em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros
'''
valorp = float(input('Qual é o valor do produto? R$'))
print('''Formas de pagamento:
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opção = int(input('Digite a opção desejada: '))
if opção == 1:
    total = valorp - (valorp * 10 / 100)
elif opção == 2:
    total = valorp - (valorp * 5 / 100)
elif opção == 3:
    total = valorp
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = valorp + (valorp * 20 / 100)
    totalparcelas = int(input('Quantas parcelas? '))
    parcela = total / totalparcelas
    print('Sua compra será parcelada em {} parcelas de R${:.2f}'.format(totalparcelas, parcela))
else:
    total = valorp
    print('Opção Inválida')
print('Sua compra de R$ {:.2f} vai custar R$ {}.'.format(valorp, total))

