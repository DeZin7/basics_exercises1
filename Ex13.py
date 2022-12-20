lista1 = []
lista2 = []
lista3 = []

for i in range (0,5):
    v1 = int(input('digite os valores da lista1:  '))
    lista1 += [v1]
for j in range(0, 5):
    v2 = int(input('digite os valores da lista2: '))
    lista2 += [v2]
lista3 = lista1 + lista2

print(lista1)
print(lista2)
print(lista3)