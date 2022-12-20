import numpy as np

X = np.zeros(10)
for i in range (0,10):
    X[i] = int(input(f'Digite o valor do elemento {i+1}: '))
    if X[i] <= 0:
        X[i] = 1

print(X)

