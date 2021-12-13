# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a temperatura em °C: '))
conv = celsius * 9 / 5 + 32
print('A temperatura {:.1f}°C em Fahrenheit será {:.1f}°F'.format(celsius, conv))