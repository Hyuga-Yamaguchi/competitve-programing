s = input()
sn = len(s)

lis_2 = []
for i in range(1 << (sn - 1)):
    lis = [0, sn]
    for j in range(sn - 1):
        if (i >> j) & 1:
            lis.append(j + 1)
    lis = sorted(lis)
    #print(lis)
    sum1 = 0
    for j in range(len(lis) - 1):
        sum1 += int(s[lis[j]:lis[j + 1]])
    lis_2.append(sum1)
#print(lis_2)
print(sum(lis_2))
