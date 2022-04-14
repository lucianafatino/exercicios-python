'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não quer continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos
'''

# Minha solução
mais18 = masc = fem20 = 0

while True:
    askidade = int(input('Idade: '))
    asksexo = str(input('Gênero [M/F]: ')).strip().upper()[0]
    sn = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if askidade > 18:
        mais18 += 1
    if asksexo == 'M':
        masc += 1
    if askidade < 20 and asksexo == 'F':
        fem20 += 1
    if sn == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {masc} homens cadastrados')
print(f'E temos {fem20} mulheres com menos de 20 anos.')

# Solução do Prof
mais18 = masc = fem20 = 0

while True:
    askidade = int(input('Idade: '))
    asksexo = ' '
    sn = ' '
    while asksexo not in 'MF':
        asksexo = str(input('Gênero [M/F]: ')).upper()[0]
    if askidade >= 18:
        mais18 += 1
    if asksexo == 'M':
        masc += 1
    if askidade < 20 and asksexo == 'F':
        fem20 += 1
    while sn not in 'SN':
        sn = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if sn == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {masc} homens cadastrados')
print(f'E temos {fem20} mulheres com menos de 20 anos.')