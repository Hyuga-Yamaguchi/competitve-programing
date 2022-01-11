a, b, c, x, y = map(int, input().split())

INF = 10 ** 12
ans = INF
for i in range(0, 2 * max(x, y) + 2, 2):
    c_cost = c * i
    a_cost = a * max(x - i // 2, 0)
    b_cost = b * max(y - i // 2, 0)
    #print(c_cost, a_cost, b_cost)
    cost = a_cost + b_cost + c_cost
    ans = min(ans, cost)
print(ans)
