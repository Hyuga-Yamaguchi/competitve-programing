n, x = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)

ans = 0
for i in range(n):
    if x > 0:
        ans += 1
        x -= a[i]
if x == 0:
    print(ans)
else:
    print(ans - 1)
