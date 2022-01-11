n, q = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

c.insert(0, 1)
c.append(1)
print(a, c)

def exp(a, n, p):
    bi = str(format(n, "b"))#2進表現に
    res = 1
    for i in range(len(bi)):
        res = (res * res) % p
        if bi[i] == "1":
            res = (res * a) % p
    return res

for i in range(q + 1):
