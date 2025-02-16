"""エラトステネスの篩
1~nまでの素数をリストで列挙
"""

def prime_eratostheness(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return set(i for i in range(n + 1) if is_prime[i])

prime_eratostheness(100)
