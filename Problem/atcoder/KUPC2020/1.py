n = int(input())
xy = list(list(map(int, input().split())) for _ in range(n))

length = 0
for i in range(n - 1):
    length += abs(xy[i][0] - xy[i + 1][0]) + abs(xy[i][1] - xy[i + 1][1])

print(length)
