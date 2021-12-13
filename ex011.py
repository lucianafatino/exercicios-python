# Faça um programa que leia a largura e a altura de uma parede em metros e calcule
# a sua área e a quantia de tinta necessária para pinta-la, sabendo que cada litro
# de tinta pinta uma área de 2m²
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
print('A dimensão da sua parede é de {}x{} e a área é de {}'.format(largura, altura, area))
tinta = area / 2
print('Você precisará de {} litros de tinta para pintar a parede'.format(tinta))