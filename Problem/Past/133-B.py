n, d = map(int, input().split())
x = list(list(map(int, input().split())) for _ in range(n))

#print(x)

lis = []
for i in range(n):
    for j in range(i + 1, n):
        #各点語との距離
        lis1 = []
        for k in range(d):
            l_x = (x[i][k] - x[j][k]) ** 2
            lis1.append(l_x)
        lis.append(sum(lis1) ** 0.5)

ans = 0
for i in range(len(lis)):
    if lis[i].is_integer() == True:
        ans += 1

print(ans)
