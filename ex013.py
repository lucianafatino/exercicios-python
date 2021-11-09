# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor do seu salário antigo: R$ '))
porcentagem = (15 / 100) * salario
novosalario = salario + porcentagem
print('O seu novo salário, com acréscimo de 15%, será de R$ {:.2f}'.format(novosalario))