h, w = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(h))

min_num = 10 ** 5
for i in range(w):
    for j in range(h):
        min_num = min(min_num, a[j][i])

ans = 0
for i in range(w):
    for j in range(h):
        ans += a[j][i] - min_num
print(ans)
