"""n <= 3000の制約で未AC"""

n = int(input())
pair = []
for i in range(n):
    X, Y = map(int, input().split())
    pair.append((X, Y))

ans = 0
import itertools
q = itertools.combinations(pair, 2)
for pi, pj in q:
    (xi, yi) = pi
    (xj, yj) = pj
    dx = xi - xj
    dy = yi - yj
    if (xi + dy, yi + dx) in pair and (xj + dy, yj + dx) in pair:
        ans = max(ans, dy ** 2 + dx ** 2)
    elif (xi + dy, yi - dx) in pair and (xj + dy, yj - dx) in pair:
        ans = max(ans, dy ** 2 + dx ** 2)
print(ans)
