import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from operator import itemgetter
import numpy as np #pypyでは使用不可
input = sys.stdin.readline
def int_input(): return int(input())
def int_map(): return map(int, input().split())
def int_list(): return list(int_map())
def int_row(N): return [int_input() for _ in range(N)]
def int_row_list(N): return [int_list() for _ in range(N)]
def str_input(): return input()
def str_map(): return input().split()
def str_list(): return list(str_map())
def str_row(N): return [str_input() for _ in range(N)]
def str_row_list(N): return [list(str_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
flaot_INF = float('inf')
INF = 1 << 60
MOD = 10 ** 9 + 7

def main():
    n, k = int_map()
    r = [None] * n; c = [None] * n
    for i in range(n):
        R, C = int_map()
        r[i] = R; c[i] = C
    g1 = [[] for _ in range(n)]
    for i in range(k):
        a, b = int_map()
        g1[a - 1].append(b - 1)
        g1[b - 1].append(a - 1)
    #print(g1)

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

    #ダイクストラ法
    def dijkstra_heap(g, n, s = 0):
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

    g2 = [[] for _ in range(n)]
    for i in range(n):
        d = bfs(g1, i)
        for j in range(n):
            if 0 < d[j] <= c[i]:
                g2[i].append([j, r[i]])

    dist = dijkstra_heap(g2, n)
    print(dist[-1])

if __name__ == '__main__':
    main()
