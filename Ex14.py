import numpy as np

t = int(input('informe um valor inteiro de T: '))
x = np.zeros(20, dtype=int)
cont = 0
while cont<20:
    for i in range (0,t):
        x[cont] = i
        cont += 1
        if cont == 20:
            break

print(x)