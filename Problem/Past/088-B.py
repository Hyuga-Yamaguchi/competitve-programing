n = int(input())
a = list(map(int, input().split()))
a = sorted(a)[::-1]

ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += a[i]
    else:
        ans -= a[i]
print(ans)
