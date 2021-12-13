# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere que U$ 1,00 = R$ 5,63 e EUR = R$ 6,35


real = float(input('Quantos reais você deseja converter? R$ '))
dolar = real / 5.63
euro = real / 6.35
print('O valor de R$ {:.2f} em dólares é de USD {:.2f}, e em euros é de EUR {:.2f}'.format(real, dolar, euro))