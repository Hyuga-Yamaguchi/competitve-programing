def prime_factorization(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

n = int(input())
lis = prime_factorization(n)
print(str(n) + ":", end = "")
for i in range(len(lis)):
    print(" " + str(lis[i]), end = "")
print("")
