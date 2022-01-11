import math

n = int(input())
xy = list(list(map(int, input().split())) for _ in range(n))

l_lis =[]
for i in range(n):
    for j in range(i + 1, n):
        l = (xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2
        l_lis.append(l)

print(math.sqrt(max(l_lis)))
