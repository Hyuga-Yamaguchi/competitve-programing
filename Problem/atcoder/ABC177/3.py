n = int(input())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    res += a[i] * a[i]
ans = sum(a) * sum(a)
print(((ans - res) // 2) % (10 ** 9 + 7))
