def bubbleSort(lista):
    for passnum in range(len(lista)-1,0,-1):
         for i in range(passnum):
             if lista[i]>lista[i+1]:
                 maior = lista[i]
                 lista[i] = lista[i+1]
                 lista[i+1] = maior


lista = [0, 20, 98, 76, 1057, 946, 34, 92, 77, 3]
bubbleSort(lista)
print(lista)
