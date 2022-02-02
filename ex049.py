'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora faça utilizando o laço for'''
n = int(input('Digite um valor: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, c*n))
