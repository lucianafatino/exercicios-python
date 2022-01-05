# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo
print('-=' * 15)
print('Analisador de Triângulos')
print('-=' * 15)
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')


