# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5 % de desconto
n1 = float(input('Digite o valor do produto: '))
desconto = (5 * n1) / 100
valor = n1 - desconto
print('O valor, com desconto de 5%, a ser pago será de R$ {:.2f}'.format(valor))
