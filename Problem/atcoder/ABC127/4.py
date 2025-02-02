import bisect
from operator import itemgetter

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
d = [None] * m
for i in range(m):
    bc = list(map(int, input().split()))
    d[i] = bc
d.sort(reverse = True, key = itemgetter(1))
#print(d)

lis = []
for b, c in d:
    lis += [c] * b
    if len(lis) > n:
        break
#print(lis)

for i in range(min(n, len(lis))):
    a[i] = max(a[i], lis[i])

#print(a)
print(sum(a))
