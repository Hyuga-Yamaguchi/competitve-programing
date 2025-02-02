n, x = map(int, input().split())
a, b, c, d = [None] * n, [None] * n, [None] * n, [None] * n
for i in range(n):
    A, B, C, D = map(int, input().split())
    a[i] = A; b[i] = B; c[i] = C; d[i] = D

min_len = 10 ** 10; max_len = 0
for i in range(n):
    cost = b[i] + ((x - a[i]) // c[i] + 1) * d[i]
    min_len = min(cost, min_len)
    max_len = max(cost, max_len)
print(min_len, max_len)
