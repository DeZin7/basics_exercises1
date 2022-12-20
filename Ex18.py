# Fibonacci

def fibonacci(n):
    if n <=1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input('digite o numero de termos da sequencia de Fibonacci que vc deseja: '))
fibonacci_soma = 0
for i in range(0, n):
    fibonacci_soma += fibonacci(i)
    print(f'{fibonacci(i)}', end=' ')
print()
print(fibonacci_soma)
