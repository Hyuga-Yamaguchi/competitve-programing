n = int(input())
ab = list(list(map(int, input().split())) for _ in range(n))

ans = 0
for i in range(n):
    a = ab[i][0]
    b = ab[i][1]
    ans += (a + b) * (b - a + 1) // 2

print(ans)
