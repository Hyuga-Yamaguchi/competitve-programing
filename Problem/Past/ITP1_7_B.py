n, x=map(int, input().split())
z1, z2=map(int, input().split())

count = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        k = x - i - j
        if 1 <= k <= n and i < j < k:
            count += 1
print(count)
