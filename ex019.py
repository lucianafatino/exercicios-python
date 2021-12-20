# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo
# o nome do escolhido.
from random import choice
# a1, a2, a3, a4 = 'Luciana', 'Mariana', 'Júlia', 'Marcos'
primeiro = input('Digite o nome do primeiro aluno: ')
segundo = input('Digite o nome do segundo aluno: ')
terceiro = input('Digite o nome do terceiro aluno: ')
quarto = input('Digite o nome do quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
print('O sorteado(a) foi {}'.format(choice(lista)))

