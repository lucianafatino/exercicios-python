'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

# Minha resolução
sexo = str(input('Qual é o seu gênero? [M/F] ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Valor Inválido. Qual é o seu gênero? [M/F] ')).upper()
print('O gênero {} foi registrado com sucesso.'.format(sexo))

# Resolução do professor
sexo = str(input('Qual é o seu gênero? [M/F] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Valor Inválido. Qual é o seu gênero? [M/F] ')).upper().upper().strip()[0]
print('O gênero {} foi registrado com sucesso.'.format(sexo))