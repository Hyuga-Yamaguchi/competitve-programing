m = int(input())
cnt = 0
d = [None] * m; c = [None] * m;
for i in range(m):
    D, C = map(int, input().split())
    d[i] = D; c[i] = C
c_sum = sum(c)

s = 0
for i in range(m):
    s += d[i] * c[i]

print((c_sum - 1) + (s - 1) // 9)
