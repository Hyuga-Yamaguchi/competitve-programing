n, m = map(int, input().split())
a = list(map(int, input().split()))
a.append(0); a.append(n + 1)
a = sorted(a)

lis = []
for i in range(m + 1):
    lis.append(a[i + 1] - a[i] - 1)
#print(lis)

l = 10 ** 9 + 1
for i in range(len(lis)):
    if lis[i] >= 1:
        l = min(l, lis[i])
#print(l)

cnt = 0
for i in range(m + 1):
    if lis[i] % l == 0:
        cnt += lis[i] // l
    else:
        cnt += lis[i] // l + 1
print(cnt)
