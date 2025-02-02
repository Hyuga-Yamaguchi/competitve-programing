"""a ** n (mod p)を求める
"""
n, m = map(int, input().split())

def exp(a, n, p):
    bi = str(format(n, "b"))#2進表現に
    res = 1
    for i in range(len(bi)):
        res = (res * res) % p
        if bi[i] == "1":
            res = (res * a) % p
    return res

print(exp(10, n, m ** 2) // m)
