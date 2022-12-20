import numpy as np
lista = []
for n in range (0,10):
    numero = float(input('digite o numero a ser add no vetor: '))
    lista += [numero]
    vetor = np.array(lista)

print(f'vetor não invertido = {vetor}')
vetor_invertido = sorted(vetor, reverse=True)
print('vetor invertido =', end=' ')
print('[ ', end='')
for i in vetor_invertido:
    print(i, end=' ')
print(']')