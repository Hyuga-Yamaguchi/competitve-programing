n = int(input())
d = list(int(input()) for _ in range(n))

d = sorted(d)

ans = 1
for i in range(n - 1):
    if d[i] < d[i + 1]:
        ans += 1
print(ans)
