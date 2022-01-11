n = int(input())

t = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        xy = list(map(int, input().split()))
        t[i].append(xy)
print(t)

ans = 0
for bit in range(1 << n):
    lis = [0] * n
    for i in range(n):
        if (bit >> i) & 1:
            lis[i] = 1
    print("lis = " + str(lis))
    u = [-1] * n; flag = False
    for i in range(n):
        if lis[i] == 1:
            for j in range(len(t[i])):
                x = t[i][j][0] - 1
                y = t[i][j][1]
                if y == 1:
                    if u[x] != 0:
                        u[x] = 1
                    else:
                        flag = True
                elif y == 0:
                    if u[x] != 1:
                        u[x] = 0
                    else:
                        flag = True
    print("u = " + str(u))
    print(flag)
    tmp = 0
    for i in range(n):
        if u[i] >= 0 and lis[i] != u[i]:
            tmp = 0
            break
        else:
            tmp = sum(lis)
    if flag:
        tmp = 0
    print("tmp = " + str(tmp))
    ans = max(ans, tmp)
print(ans)
