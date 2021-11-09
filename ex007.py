# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média
notaum = int(input('Digite a primeira nota: '))
notadois = int(input('Digite a segunda nota: '))
media = (notaum + notadois) / 2
print('A média do aluno é {:.2f}'.format(media))