# Escreva um programa que pergunte o salario de um funcionário e calcule o valor de seu aumento
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para inferiores ou iguais, o aumento é de 15%
salario = float(input('Qual é o seu salário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('Seu novo salário, com reajuste de 15% passará a ser R$ {:.2f}'.format(novo))
else:
    novo = salario + (salario * 10 / 100)
    print('Seu novo salário, com reajuste de 10% será de R$ {:.2f}'.format(novo))