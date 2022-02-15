'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
print('=' * 30)
print('GERADOR DE UMA PA'.center(30))
print('=' * 30)

inicio = int(input('Primeiro termo: '))
passo = int(input('Razão da PA: '))
termo = inicio
cont = 1
total = 0
mais = 10
print('A PA será: ')
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ↠ '.format(termo), end="")
        termo += passo
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))