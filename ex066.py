'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando
o flag.
'''
c = n = s = 0
while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores foi {s}!')

# Solução do professor
'''
soma = c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
        if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores foi {s}!')
'''

















