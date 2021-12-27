# Crie um programa que leia o nome completo de uma pessoa e mostre
nome = str(input('Digite o seu nome completo: ')).strip()

# O nome com todas as letras maiúsculas
print('O nome em letras maiúsculas é {}'.format(nome.upper()))

# O nome com todas as letras minúsculas
print('O nome em letras minúsculas é {}'.format(nome.lower())) # ou ncf = nome.casefold()

# Quantas letras tem no total - sem considerar espaços
print('O total de letras do nome completo é {}'.format(len(nome) - nome.count(" ")))

# Quantas letras tem o primeiro nome
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#ou
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))






