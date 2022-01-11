a, b, c ,x ,y = map(int, input().split())
INF = 10 ** 12

ans = INF
max_xy = max(x, y)
for i in range(0, max_xy + 1):
    cost = 2 * c * i
    if x - i >= 0:
        cost += a * (x - i)
    if y - i >= 0:
        cost += b * (y - i)
    if ans >= cost:
        ans = cost
print(ans)
