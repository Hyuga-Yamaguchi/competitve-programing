
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n
dp[0] = a[0] * b[0]
max_a = 0
for i in range(n):
    max_a = max(max_a, a[i])
    cur = max_a * b[i]
    dp[i] = max(dp[i - 1], cur)

for i in range(n):
    print(dp[i])
