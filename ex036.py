''' Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o empréstimo
será negado '''
valorDaCasa = float(input('Qual é o valor da casa? R$ '))
salário = float(input('Qual é o salário? R$ '))
qtdAnos = int(input('Em quantos anos você pretente pagar? '))
valorPrestação = valorDaCasa / (qtdAnos * 12)
min = salário * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valorDaCasa, qtdAnos, valorPrestação))
if valorPrestação <= min:
    print('Empréstimo APROVADO')
else:
    print('Empréstimo NEGADO')