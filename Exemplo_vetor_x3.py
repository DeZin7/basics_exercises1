import numpy

n = int(input('informe o numero de elementos: '))
A = numpy.empty(n)

for i in range(0,n):
    A[i] = int(input(f'informe o elemento da posição {i+1}: '))

for i in range(0,n):
    A[i] = A[i]*3

print('imprimindo o vetor na tela...')
print('[', end='')
for i in range (0,n):
    if i<(n-1):
        print(f'{A[i]}', end=' ')
    else:
        print(f'{A[i]}]')



