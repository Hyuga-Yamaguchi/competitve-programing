from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

d = list(Counter(a).items())

values = []
for i in range(len(d)):
    values.append(d[i][1])

values = sorted(values)
#print(d, values)

ans = 0
for i in range(len(values) - k):
    ans += values[i]

print(ans)
