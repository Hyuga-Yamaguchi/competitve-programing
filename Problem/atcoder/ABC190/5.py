import sys
input = sys.stdin.readline

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
#print(g)

k = int(input())
c = list(map(int, input().split()))
for i in range(k):
    c[i] -= 1
#print(c)

from collections import deque

def bfs(u):
    queue = deque([u])
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return [d[i] for i in c]

dist = [bfs(i) for i in c]
#print(dist)

if None in dist[0]:
    print(-1)
    exit()

INF = 10 ** 9
#メモ化再帰
dp = [[-1] * k for _ in range(1 << k)]
def rec(bit, v):
    #すでに探索済ならリターン
    if dp[bit][v] != -1:
        return dp[bit][v]

    #初期値
    if bit == (1 << v):
        dp[bit][v] = 0
        return dp[bit][v]

    #答えを格納する変数
    res = INF

    #bitのvを除いたもの
    prev_bit = bit & ~(1 << v)

    #vの手前のノードとしてuを全探索
    for u in range(k):
        if not prev_bit & (1 << u): #uがprev_bitになかったらダメ
            continue

        #再帰的に探索
        if res > rec(prev_bit, u) + dist[u][v]:
            res = rec(prev_bit, u) + dist[u][v]

    dp[bit][v] = res
    return dp[bit][v]

#探索
res = INF
for v in range(k):
    if res > rec((1 << k) - 1, v):
        res = rec((1 << k) - 1, v)
    #print(v, dp)
print(res + 1)
