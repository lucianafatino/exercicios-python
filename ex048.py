'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que
se encontram no intervalo de 1 até 500'''
soma = 0 # acumulador
cont = 0 # contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 # toda vez que ele achar um número divisivel por três ele fará ficará guardado no cont
        soma += c
print('A soma dos {} números solicitados é {}'.format(cont, soma))
