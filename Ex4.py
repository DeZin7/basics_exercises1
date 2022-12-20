#Um número n >= 100 e n<= 999. Imprimir separadamente os dígitos que representam
#as unidades, dezenas e centenas do número.

n = int(input('Digite um número entre 100 e 999: '))
while n<100 or n>=999:
    n = int(input('Número inválido! Digite entre 100 e 999: '))
a = str(n)
print(f'centena: {a[0]}')
print(f'dezena: {a[1]}')
print(f'unidade: {a[2]}')