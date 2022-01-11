n = int(input())
ab = list(list(map(int, input().split())) for _ in range(n))

print(n, ab)

time_lis = []
for j in range(100 + 1):
    for k in range(j + 1, 100 + 1):
        time_sum = 0
        for i in range(n - 1):
            time = abs(j - ab[i][0]) + abs(ab[i][0] - ab[i][1]) + abs(ab[i][1] - k)
            time_sum += time
            time_lis.append(time_sum)

print(time_lis)
print(min(time_lis))
