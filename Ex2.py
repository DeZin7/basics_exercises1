# Dois floats de dupla precisão A e B = 2 notas de um aluno.
# Calcular a média do aluno, sabendo q a nota A tem peso 3.5
# nota B tem peso 7.5. Cada nota vai de 0 até 10.0, sempre com uma casa decimal

A = float(input('Nota 1: '))
while A < 0 or A > 10:
    A = float(input('Valor inválido! Digite um valor entre 0 e 10:  '))
B = float(input('Nota 2: '))
while B < 0 or B > 10:
    B = float(input('Valor inválido! Digite um valor entre 0 e 10:  '))
pA = 3.5
pB = 7.5

média = ((pA*A)+(pB*B))/(pA+pB)
print(f'A média final foi {média:.1f}')
