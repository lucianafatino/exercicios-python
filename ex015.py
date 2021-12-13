# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
da = int(input('Quantos dias o carro foi alugado? '))
kc = float(input('Quantos quilômetros percorreu o carro? '))
preco = (da * 60) + (kc * 0.15)
print('O valor a ser pago será de R$ {:.2f}'.format(preco))
