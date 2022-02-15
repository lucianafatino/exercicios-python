'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar
ao usuário se ele quer continuar ou não a digitar mais valores.
'''
resposta = 'S'
soma = qtd = media = maior = menor = 0
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
media = soma / qtd
print('Você digitou {} números e a média foi {}'.format(qtd, media))
print('O menor número foi {} e maior número foi {}.'.format(menor, maior))
