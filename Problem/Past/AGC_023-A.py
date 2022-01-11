from collections import Counter

n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1):
    a[i + 1] += a[i]

lis = list(Counter(a).items())

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

ans = 0
for i in range(len(lis)):
    if lis[i][1] >= 2:
        ans += cmb(lis[i][1], 2)
    if lis[i][0] == 0:
        ans += lis[i][1]
print(ans)
