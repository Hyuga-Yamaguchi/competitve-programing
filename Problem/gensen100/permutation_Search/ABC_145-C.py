import itertools
import math

n = int(input())
xy = list(list(map(int, input().split())) for _ in range(n))

ans = 0
for i in itertools.permutations(xy):
    for j in range(len(i) - 1):
        ans += math.sqrt((i[j][0] - i[j + 1][0]) ** 2 + (i[j][1] - i[j + 1][1]) ** 2)
print(ans / len(list(itertools.permutations(xy))))
