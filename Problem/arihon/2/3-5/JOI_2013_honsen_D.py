import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from operator import itemgetter
#import numpy as np
input = sys.stdin.readline
def int_input(): return int(input())
def int_map(): return map(int, input().split())
def int_list(): return list(int_map())
def int_row(N): return [int_input() for _ in range(N)]
def int_row_list(N): return [int_list() for _ in range(N)]
def str_input(): return input()[:-1]
def str_map(): return input().split()
def str_list(): return list(str_map())
def str_row(N): return [str_input() for _ in range(N)]
def str_row_list(N): return [list(str_map()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 10 ** 9 + 7
mod = 998244353
lower_start = 97 #"a"のASCIIコード
upper_start = 65 #"A"のASCIIコード
number_start = 48 #"0"のASCIIコード

#メモリ消費を抑える時はグローバル空間に書く
def main():
    #ダイクストラ法
    def dijkstra_heap(s, n, g, x):
        dist = [INF] * n
        dist[s] = 0
        seen = [False] * n
        seen[s] = True
        cur = x

        #(d[v], v)のペアを要素としたヒープを作る
        hq = [(dist[s], s, cur)]

        while hq:
            if seen[-1]:
                break
            #v:使用済みでない頂点のうち、d[v]が最小の頂点
            #d:vに対するキー値
            c, v, pos = heappop(hq)
            #print('-----------------------')
            #print('hq', c, v, pos)
            if dist[v] < c:
                continue
            seen[v] = True
            for to, cost in g[v]:
                if not seen[to]:
                    #print('to, cost, c, pos', to, cost, c, pos)
                    #届かない時
                    if pos < cost:
                        if cost > h[v]:
                            continue
                        dist[to] = dist[v] + cost + (cost - pos)
                        pos = 0
                        #print('flag0')
                    #普通に届く時
                    elif cost <= pos <= h[to] + cost:
                        dist[to] = dist[v] + cost
                        pos -= cost
                        #print('flag1')
                    #上行ってる時
                    elif pos > h[to] + cost:
                        dist[to] = dist[v] + cost + (pos - h[to] - cost)
                        pos = h[to]
                        #print('flag2')
                    #print('dist[to], to, pos', dist[to], to, pos)
                    heappush(hq, (dist[to], to, pos))
        return dist

    n, m, x = int_map()
    h = [None] * n
    for i in range(n):
        h[i] = int_input()
    h = h + [0]

    abt = [None] * m
    for i in range(m):
        a, b, t = int_map()
        a -= 1; b -= 1
        abt[i] = [a, b, t]
    abt = abt + [[n - 1, n, h[n - 1]]]

    #グラフを張る 飛べない変があるので注意
    g = [[] for _ in range(n + 1)]
    for i in range(m + 1):
        (a, b, t) = abt[i]
        if t > h[a] and t <= h[b]:
            g[b].append((a, t))
        elif t <= h[a] and t > h[b]:
            g[a].append((b, t))
        elif t <= h[a] and t <= h[b]:
            g[a].append((b, t))
            g[b].append((a, t))
    #print(g)

    dist = dijkstra_heap(0, n + 1, g, x)
    #print(dist)

    if dist[-1] >= INF:
        print(-1)
    else:
        print(dist[-1] - h[n - 1])

if __name__ == '__main__':
    main()
