'''Crie um programa que leia uma frase qualquer e diga se ela é um palídromo, desconsiderando os espaços
*** Palíndromos são palavras que, se lidas de trás para frente e de frente para trás, serão a mesma coisa
ex: apos a sopa
    a sacada da casa
    a torre da derrota
    o lobo ama o bolo
    anotaram a data da maratona
'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# inverso = junto[::-1] // tirando o for, podemos usar esta forma simplificada de verificar palíndromos
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')