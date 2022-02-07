'''Desenvolva um programa que leia: nome, idade e sexo de quatro pessoas. No final do programa, mostre:
    - A média de idade do grupo
    - Qual é o nome do homem mais velho
    - Quantas mulheres têm menos de 20 anos'''
somaIdade = 0
maiorHomem = 0
nomeMaisVelho = ''
totMulherVinte = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        maiorHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > maiorHomem:
        maiorHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulherVinte += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorHomem, nomeMaisVelho))
print('Ao todo, são {} mulheres com menos de 20 anos.'.format(totMulherVinte))