# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente
# Exemplo:
    # Ana Maria de Souza
    # primeiro = Ana
    # ultimo = Souza
n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome)-1]))