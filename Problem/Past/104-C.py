d, g = map(int, input().split())
pc = list(list(map(int, input().split())) for _ in range(d))

num = 0
scr_full = []
for i in range(1 << d):
    lis = []
    for j in range(d):
        if (i >> j) & 1:
            lis.append(j + 1)
    #print(lis)
    scr = [0]
    que_num = []
    for j in range(len(lis)):
        scr.append(pc[lis[j] - 1][0] * 100 * lis[j] + pc[lis[j] - 1][1])
        que_num.append(pc[lis[j] - 1][0])
    #print(scr)
    scr_full.append([sum(scr), lis, sum(que_num)])
print(sorted(scr_full))
l = len(scr_full)
for k in range(l):
     if scr_full[k][0] >= g:
