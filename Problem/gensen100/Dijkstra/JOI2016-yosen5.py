import sys
from collections import Counter, deque
from heapq import heapify, heappop, heappush
input = sys.stdin.readline
def int_input(): return int(input())
def int_map(): return map(int, input().split())
def int_list(): return list(int_map())
def int_row(N): return [int_input() for _ in range(N)]
def int_row_list(N): return [int_list() for _ in range(N)]
INF = 1 << 60

def main():
    def bfs(g, u):
        queue = deque([u])
        d = [None] * n # uからの距離の初期化
        d[u] = 0 # 自分との距離は0
        while queue:
            v = queue.popleft()
            for i in g[v]:
                if d[i] is None:
                    d[i] = d[v] + 1
                    queue.append(i)
        return d

    #入力
    n, m, k, s = int_map()
    p, q = int_map()
    zombie = [None] * k
    for i in range(k):
        z = int_input()
        zombie[i] = z - 1

    g = [[] for _ in range(n)]
    for i in range(m):
        a, b = int_map()
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    zombie_dist = [INF] * n
    for i in zombie:
        d = bfs(g, i)
        for j in range(n):
            zombie_dist[j] = min(zombie_dist[j], d[j])
    #print(zombie_dist)

    danger_town = set([])
    for i in range(n):
        if 0 < zombie_dist[i] <= s:
            danger_town.add(i)
    #print(danger_town)

    g2 = [[] for _ in range(n)]
    for i in range(n):
        for j in g[i]:
            if j in zombie:
                g2[i].append([j, INF])
            elif j in danger_town:
                g2[i].append([j, q])
            else:
                g2[i].append([j, p])
    #print(g)
    #print(g2)
    #ダイクストラ法
    def dijkstra_heap(g, s, n):
        dist = [INF] * n
        dist[s] = 0

        #(d[v], v)のペアを要素としたヒープを作る
        hq = [(dist[s], s)]

        while hq:
            #v:使用済みでない頂点のうち、d[v]が最小の頂点
            #d:vに対するキー値
            c, v = heappop(hq)
            if dist[v] < c:
                continue
            for to, cost in g[v]:
                if dist[v] + cost < dist[to]:
                    dist[to] = dist[v] + cost
                    heappush(hq, (dist[to], to))
        return dist

    dist = dijkstra_heap(g2, 0, n)
    #print(dist)
    if n - 1 in danger_town:
        print(dist[-1] - q)
    else:
        print(dist[-1] - p)

if __name__ == '__main__':
    main()
