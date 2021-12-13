# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média
notaum = float(input('Digite a primeira nota: '))
notadois = float(input('Digite a segunda nota: '))
media = (notaum + notadois) / 2
print('A média do aluno é {:.1f}'.format(media))