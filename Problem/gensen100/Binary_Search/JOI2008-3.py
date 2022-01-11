import bisect

n, m = map(int, input().split())
p = list(int(input()) for _ in range(n))
p.append(0)

x = set()
#２つのpの全通りの和を求める
q = []
for i in range(n + 1):
    for j in range(n + 1):
        x.add(p[i] + p[j])
q = list(x)
q.sort()
#print(q)
nq = len(q)

#２つのqのリストからm以下の最大値を求める
max_value = 0
for i in range(nq):
    iter = bisect.bisect_left(q, m - q[i])
    val = q[iter - 1]
    #print(val)
    if m >= q[i] + val > max_value:
        max_value = q[i] + val
print(max_value)
