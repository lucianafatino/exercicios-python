'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50'''
for c in range(1, 50+1): # faz duas iterações
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')

# Resolução do prof
for c in range(2, 51, 2): # faz menos iteração
    print(c, end=' ')
print('FIM')


