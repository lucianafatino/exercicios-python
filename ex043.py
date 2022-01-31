'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre o status, de
acordo com a tabela abaixo:
    - Abaixo de 18.5: ABAIXO DO PESO
    - Entre 18.5 e 25: PESO IDEAL
    - 25 até 30: SOBREPESO
    - 30 até 40: OBESIDADE
    - Acima de 40: OBESIDADE MÓRBIDA
'''
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura**2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('Você está com o PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA.')
