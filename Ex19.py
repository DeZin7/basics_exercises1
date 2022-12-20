import numpy as np

def soma(x):
    print(x)
    soma_elementos = 0
    for i in range(0,n):
        soma_elementos += x[i]
    print(f'a soma dos elementos é {soma_elementos}')


n = int(input('digite o numero de elementos no vetor: '))
x = np.zeros(n, dtype=int)
for i in range(0,n):
    x[i] = int(input(f'digite o elemento {i} do vetor: '))
soma(x)