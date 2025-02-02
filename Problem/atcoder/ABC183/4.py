import operator

length = 2 * (10 ** 5)

n, w = map(int, input().split())
stp = list(list(map(int, input().split())) for _ in range(n))

#stp = sorted(stp, key = operator.itemgetter(1))
#print(stp)
a = [0] * (length + 1)

for i in range(n):
    a[stp[i][0]] += stp[i][2]
    a[stp[i][1]] -= stp[i][2]

#print(a)

for i in range(1, len(a)):
    a[i] = a[i - 1] + a[i]

#print(a)

if max(a) > w:
    print("No")
else:
    print("Yes")
