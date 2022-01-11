import itertools
import math

lis = list(itertools.permutations(range(1, 7)))

u = [[0] * 3 for _ in range(2)]
cnt = 0
for i in range(len(lis)):
    u[0][0] = lis[i][0]
    u[0][1] = lis[i][1]
    u[0][2] = lis[i][2]
    u[1][0] = lis[i][3]
    u[1][1] = lis[i][4]
    u[1][2] = lis[i][5]
    #print(u)
    if math.gcd(u[0][0], u[0][1]) == 1 and math.gcd(u[0][0], u[1][0]) == 1:
        if math.gcd(u[0][1], u[0][2]) == 1 and math.gcd(u[0][1], u[1][1]) == 1:
            if math.gcd(u[0][2], u[1][2]) == 1:
                if math.gcd(u[1][1], u[1][0]) == 1 and math.gcd(u[1][1], u[1][2]) == 1:
                    cnt += 1
print(cnt)
