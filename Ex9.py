caracteres = str(input('digite 10 caracteres: ')).upper()
cont = 0
if len(caracteres) != 10:
    print('Você não digitou 10 caracteres!!!')
else:
    for i in caracteres:
        if i not in 'AEIOU':
            cont += 1
print(f'Foram digitadas {cont} consoantes.')


