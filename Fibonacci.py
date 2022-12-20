def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10
if n_terms <= 0:
    print('entrada inválida...informe numero positivo')
else:
    print('serie de fibonacci: ')
    for i in range(0, n_terms):
        print(recursive_fibonacci(i), end=' ')