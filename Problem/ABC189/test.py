from decimal import Decimal

n, x = map(int, input().split())
v, p = [], []
for i in range(n):
    V, P = map(int, input().split())
    v.append(V); p.append(P)

tmp = 0
for i in range(n):
    tmp += Decimal(str(v[i])) * Decimal(str(p[i])) / 100
    print(tmp)
    if x < tmp:
        print(i + 1)
        exit()
print(-1)
