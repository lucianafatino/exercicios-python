# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere que U$ 1,00 = R$ 5,54

realm = float(input('Quantos reais você deseja converter para dólares? '))
dolarm = float(input('Favor digitar a cotação atual do dólar: '))
realcon = realm / dolarm
print('O valor R$ {} convertido para dólares é U$ {:.2f}'.format(realm, realcon))