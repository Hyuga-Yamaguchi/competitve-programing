n, m = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))

#print(n, m ,a)

point_lis2 = []
for i in range(m):
    for j in range(i + 1, m):
        point_lis = []
        for k in range(n):
            point = max([a[k][i],a[k][j]])
            point_lis.append(point)
        #print(point_lis)
        point_lis2.append(sum(point_lis))

#print(point_lis2)
print(max(point_lis2))
