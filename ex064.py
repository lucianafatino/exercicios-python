'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final,  mostre quantos
números foram digitados e qual foi a soma entre eles, desconsiderando o flag.
'''
num = qtdNumeros = soma = 0
num = int(input('Digite um número inteiro [999 para sair]: '))
while num != 999:
    qtdNumeros += 1
    soma += num
    num = int(input('Digite um número inteiro [999 para sair]: '))
print('Foram digitados {} números'.format(qtdNumeros))
print('A soma dos números digitados (desconsiderando o 999) foi {}'.format(soma))

