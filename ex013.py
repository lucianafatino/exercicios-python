# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o seu salário: R$ '))
reajuste = salario + (salario * 15 / 100)
print('O seu salário de R$ {:.2f}, após o aumento de 15%, passará a ser R$ {:.2f}'.format(salario, reajuste))