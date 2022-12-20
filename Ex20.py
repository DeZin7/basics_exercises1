import numpy as np

def qtd_pares(x):
    pares = 0
    for i in range (0,n):
        if x[i] % 2 == 0:
            pares += 1
    print(f'o vetor possui {pares} números pares!')



n = int(input('digite o tamanho do vetor: '))
x = np.zeros(n, dtype=int)
for i in range (0,n):
    x[i] = int(input(f'digite o elemento {i}: '))

qtd_pares(x)
