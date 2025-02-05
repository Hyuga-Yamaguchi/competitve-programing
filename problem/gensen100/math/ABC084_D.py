def prime_eratostheness(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return set(i for i in range(n + 1) if is_prime[i])

lis = prime_eratostheness(10 ** 5)

u = [0] * (10 ** 5 + 1)
for i in range(2, 10 ** 5 + 1):
    if i in lis and (i + 1) // 2 in lis:
        u[i] = u[i - 1] + 1
    else:
        u[i] = u[i - 1]
#print(u)

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(u[r] - u[l - 1])
