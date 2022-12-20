#ler numeor de funcionarios
#ler numero de horas trabalhadas
#valor q recebe por hora
#calcular o salário

numero = int(input('Digite o numero do funcionario: '))
horas = int(input('Digite o numero de horas trabalhadas: '))
valor = float(input('Digite o valor recebido por hora: R$ '))
salario = horas * valor
print('-='*30)
print(f'O salário do funcionario {numero} é R$ {salario:.2f}')
