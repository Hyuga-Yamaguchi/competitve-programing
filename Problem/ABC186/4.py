n = int(input())
a = list(map(int, input().split()))

a = sorted(a)

ans = 0
for i in range(n):
    ans += (- n + 1 + 2 * i) * a[i]
print(ans)
