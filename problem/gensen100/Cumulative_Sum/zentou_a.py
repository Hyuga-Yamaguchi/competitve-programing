n = int(input())
a = list(map(int, input().split()))

u = [0] * (n + 1)
u[0] = 0
for i in range(1, n + 1):
    u[i] = u[i - 1] + a[i - 1]
#print(u)

for i in range(1, n + 1):
    ans = 0
    for j in range(n + 1):
        if j + 1 >= i:
            ans = max(ans, u[j] - u[j - i])
    print(ans)
