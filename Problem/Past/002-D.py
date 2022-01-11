import itertools as it

n, m = map(int, input().split())
xy = list(list(map(int, input().split())) for _ in range(m))
#print(xy)

tmp = 0
for i in range(1 << n):
    lis = []
    for j in range(n):
        if (i >> j) & 1:
            lis.append(j + 1)
    #print("lis = " + str(lis))
    if len(lis) >= 2:
        lis_2 = list(it.combinations(lis, 2))
        #print("lis_2 = " + str(lis_2))
        cnt = 0
        for k in range(len(lis_2)):
            if list(lis_2[k]) in xy:
                #print("list(lis_2[k]) = " + str(list(lis_2[k])))
                cnt += 1
            #print("cnt = " + str(cnt))
            if cnt == len(lis_2) and tmp <= len(lis):
                tmp = len(lis)
                #print("len(lis) = " + str(len(lis)))
if tmp == 0:
    print(1)
else:
    print(tmp)
