#A, B, C são três notas de um aluno. Calcular a média sabendo que:
# nota A tem peso 2, nota B tem peso 3 e nota C tem peso 5. Cada
# nota vai de 0 à 10.0 sempre com uma casa decimal.

a = float(input('nota 1: '))
while a < 0 or a > 10:
    a = float(input('Valor inválido! Digite um valor entre 0 e 10:  '))
b = float(input('nota 2: '))
while b < 0 or b > 10:
    b = float(input('Valor inválido! Digite um valor entre 0 e 10:  '))
c = float(input('nota 3: '))
while c < 0 or c > 10:
    c = float(input('Valor inválido! Digite um valor entre 0 e 10:  '))
pa = 2
pb = 3
pc = 5
média = ((pa*a)+(pb*b)+(pc*c))/(pa+pb+pc)

print(f'a média final do aluno foi {média:.1f}')
