# (n) * (n-1) * (n-3) * (n-4)
# def fatorial(n):
#     m = 1
#     for i in range(n, 1, -1):
#         m *= i
#     return m

def fatorial_rec(n):
    if n ==1:
        return 1
    else:
        return n*fatorial_rec(n-1)


n = int(input('digite o numero o qual será calculado o fatorial: '))
print(f'{n}! = {fatorial_rec(n)}')