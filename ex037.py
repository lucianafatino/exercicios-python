''' Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual irá ser a
base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''
from time import sleep
numUsuário = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal
''')
pedeUsuário = int(input('Escolha o número correspondente à opção desejada: '))
sleep(1)
print('-=' * 25)
if pedeUsuário == 1:
    print('A base de conversão escolhida foi o Binário')
    print('O número {} convertido para binário passa a ser {}'.format(numUsuário, bin(numUsuário)[2:]))
elif pedeUsuário == 2:
    print('A base de conversão escolhida foi o Octal')
    print('O número {} convertido para octal passa a ser {}'.format(numUsuário, oct(numUsuário)[2:]))
elif pedeUsuário == 3:
    print('A base de conversão escolhida foi o Hexadecimal')
    print('O número {} convertido para hexadecimal passa a ser {}'.format(numUsuário, hex(numUsuário)[2:]))
else:
    print('Opção Inválida')
print('-=' * 25)