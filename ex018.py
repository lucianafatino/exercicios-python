# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, coseno e tangente desse angulo
from math import radians, sin, tan, cos
an = int(input('Digite um ângulo qualquer: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O ângulo {} tem o SENO de {:.2f}'.format(an, sen))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(an, cos))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(an, tan))

