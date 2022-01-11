n, q = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
c.insert(0, 1); c.append(1)
MOD = 10 ** 9 + 7

u = [0] * (n - 1)
u[0] = pow(a[0], a[1], MOD)
for i in range(1, n - 1):
    u[i] = pow(a[i], a[i + 1], MOD) + u[i - 1]
u.insert(0, 0)
#print(u)

ans = 0
for i in range(q + 1):
    ans += abs(u[c[i + 1] - 1] - u[c[i] - 1]) % MOD
    #print(u[c[i + 1] - 1], u[c[i] - 1])
print(ans % MOD)
