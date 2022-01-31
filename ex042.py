''' Refaça o desafio 035, dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    - EQUILÁTERO: Todos os lados iguais
    - ISÓSCELES: Dois lados iguais
    - ESCALENO: Todos os lados diferentes
'''
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM formar um triângulo.')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos NÃO PODEM formar um triângulo.')