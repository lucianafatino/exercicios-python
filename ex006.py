# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('Digite um número: '))
print('O dobro de {} é {} \nO triplo é {} \nSua raiz quadrada é {:.2f}'.format(n1, (n1 * 2), (n1 * 3), (n1 ** (1/2))))