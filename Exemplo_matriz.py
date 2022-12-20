import numpy as np

numero_linhas = int(input('digite o numero de linhas: '))
numero_colunas = int(input('digite o numero de colunas: '))

A = np.empty( (numero_linhas, numero_linhas) )

for i in range(0,numero_linhas):
    for j in range(0,numero_colunas):
        elemento = int(input(f'digite o elemento A{[i]}{[j]}: '))
        A[i][j] = elemento

print('imprimindo a matriz...')
for i in range(0,numero_linhas):
    for j in range(0,numero_colunas):
        print(A[i][j], end=' ')
    print()
print()