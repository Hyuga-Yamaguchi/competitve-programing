import itertools

n, m = map(int, input().split())
xy = list(list(map(int, input().split())) for _ in range(m))

tmp = 0
for bit in range(1 << n):
    lis = []
    for i in range(n):
        if (bit >> i) & 1:
            lis.append(i + 1)
    #print(lis)
    if len(lis) >= 2:
        c = list(itertools.combinations(lis, 2))
        #print(c)
        cnt = 0
        for j in range(len(c)):
            if list(c[j]) in xy:
                cnt += 1
        if cnt == len(c):
            tmp = max(tmp, len(lis))

if tmp == 0:
    print(1)
else:
    print(tmp)
