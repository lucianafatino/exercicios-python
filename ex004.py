#Faça um programa que leia algo pelo teclado e  mostre na tela
#o seu tipo primitivo e todas as informações possiveis sobre ela

teste = input('Digite algo: ')
print('Esse valor é ', type(teste))
print('Tem espaços? ', teste.isspace())
print('É número? ', teste.isnumeric())
print('É alfabetico? ', teste.isalpha())
print('É alfanumerico? ', teste.isalnum())
print('Está em maiúsculas', teste.isupper())
print('Está em minúsculas? ', teste.islower())
print('Está capitalizada? ', teste.islower())
