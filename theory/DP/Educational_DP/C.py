n = int(input())
a, b, c = [], [], []
for i in range(n):
    ai, bi, ci = map(int, input().split())
    a.append(ai); b.append(bi); c.append(ci)
#print(a, b, c)

#i日目に行動jをした場合のi日目までの最大値
dp = [[0] * 3 for _ in range(n)]

#print(dp)

#初期条件
dp[0][0], dp[0][1], dp[0][2] = a[0], b[0], c[0]

for i in range(n - 1):
    for j in range(3):
        if j == 0:
            dp[i + 1][j] = max(dp[i][1] + a[i + 1], dp[i][2] + a[i + 1])
        if j == 1:
            dp[i + 1][j] = max(dp[i][0] + b[i + 1], dp[i][2] + b[i + 1])
        if j == 2:
            dp[i + 1][j] = max(dp[i][0] + c[i + 1], dp[i][1] + c[i + 1])

#print(dp)
print(max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))
