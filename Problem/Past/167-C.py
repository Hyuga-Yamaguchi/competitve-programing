n, m, x = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))

#print(n, m, x, a)

#0b00・・・０~0b111・・・１を全部作成
cost_lis = []
abl_lis = []
for i in range(1 << n):
    cost = 0
    abl_sum = [0] * m
    #print(abl_sum)
    for j in range (len(a)):
        mask = 1 << j
        if i & mask:
            cost += a[j][0]
            for k in range(m):
                abl_sum[k] += a[j][k + 1]
    cost_lis.append(cost)
    abl_lis.append(abl_sum)
    #print(bin(i))
#print(cost_lis, abl_lis)

cost_new_lis = []
for i in range(len(abl_lis)):
    if min(abl_lis[i]) >= x:
        cost_new_lis.append(cost_lis[i])
    else:
        pass
#print(cost_new_lis)

if cost_new_lis == []:
    print(-1)
else:
    print(min(cost_new_lis))
