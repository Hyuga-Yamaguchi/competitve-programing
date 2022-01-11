import math
from decimal import Decimal

n, m = map(int, input().split())
x = [None] * (n + m); y = [None] * (n + m); r = [None] * (n + m)
for i in range(n):
    X, Y, R= map(int, input().split())
    x[i] = X; y[i] = Y; r[i] = R
for i in range(m):
    X, Y = map(int, input().split())
    x[i + n] =X; y[i + n] = Y
#print(x, y, r)

INF = 10 ** 9
ans = INF
for i in range(n + m):
    for j in range(i + 1, n + m):
        length = Decimal(str(math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)))
        if r[i] == None and r[j] == None:
            ans = min(ans, length / 2)
        elif r[i] == None and r[j] != None:
            ans = min(ans, length - r[j])
        elif r[i] != None and r[j] == None:
            ans = min(ans, length - r[i])
        else:
            ans = min(ans, r[i], r[j])
print(ans)
