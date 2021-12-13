# Escreva um programa que leia um valor em metros e converta ele em centímetros e milimetros
n1 = float(input('Uma distância em metros: '))
cen = n1 * 100
mi = n1 * 1000
km = n1 / 1000
hec = n1 / 100
dam = n1 / 10
dm = n1 * 10
print('A medida de {:.1f} metros corresponde a:\n{:.0f} cm\n{:.0f} mm\n{:.3f} km\n{:.2f} hm\n{:.1f} dam\n{:.0f} dm'.format(n1, cen, mi, km, hec, dam, dm))

#teste