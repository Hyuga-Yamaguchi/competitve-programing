a, b, c = map(int, input().split())

mod = 998244353

ans = 1
ans *= ((1 + a) * a // 2) % mod
ans *= ((1 + b) * b // 2) % mod
ans *= ((1 + c) * c // 2) % mod

print(ans % mod)
