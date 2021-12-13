# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5 % de desconto
n1 = float(input('Digite o valor do produto: R$ '))
desconto = n1 - (n1 * 5 / 100)
print('O produto que custava R$ {}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(n1, desconto))
