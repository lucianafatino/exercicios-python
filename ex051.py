'''Desenvolva um programa que leia o primeiro termo e a razao de uma PA (progressão aritimética). No final,
mostre os 10 primeiros termos dessa progressão'''
print('=' * 30)
print('10 TERMOS DE UMA PA'.center(30))
print('=' * 30)

inicio = int(input("Primeiro elemento: "))
passo = int(input("Passo: "))
fim = inicio + (10-1)*passo
fim += 1
for c in range(inicio, fim, passo):
    print(c,end=' ↠ ')
print('ACABOU')