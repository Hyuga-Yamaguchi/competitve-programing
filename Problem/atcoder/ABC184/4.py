a, b, c = map(int, input().split())

dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
#print(dp)
def func(x, y, z):
    if dp[x][y][z]:
        return dp[x][y][z]
    if x == 100 or y == 100 or z == 100:
        return 0
    dp[x][y][z] += (func(x + 1, y, z) + 1) * x /(x + y + z)
    dp[x][y][z] += (func(x, y + 1, z) + 1) * y /(x + y + z)
    dp[x][y][z] += (func(x, y, z + 1) + 1) * z /(x + y + z)
    return dp[x][y][z]

#print(dp)
print(func(a, b, c))
