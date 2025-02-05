s = int(input())

def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

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


x = s // 3
ans = 0
for i in range(1, x + 1):
    #数列の個数 i
    #残りの数 y
    y = s - 3 * i
    #数列の個数
    ans += cmb(y + i - 1, i - 1)
print(ans % (10 ** 9 + 7))
