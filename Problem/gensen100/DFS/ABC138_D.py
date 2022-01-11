import sys
sys.setrecursionlimit(10 ** 9)

def dfs(v, p, cost):
    value[v] += cost
    print("value1 = " + str(value))
    for i in g[v]:
        if not i == p:
            dfs(i, v, value[v])
            print("value2 = " + str(value))

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

#print(g)
value = [0] * n
for i in range(q):
    P, X = map(int, input().split())
    value[P - 1] += X

now = 0
parent = 0
cost = 0
dfs(now, parent, cost)
print(*value)
