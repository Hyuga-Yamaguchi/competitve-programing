import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from operator import itemgetter
#import numpy as np #pypyでは使用不可
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
def str_row_list(N): return [list(str_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 10 ** 9 + 7
mod = 998244353

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n, m = int_map()
    g = [[] for _ in range(n)]
    for i in range(m):
        a, b, c, d = int_map()
        g[a - 1].append([b - 1, c, d])
        g[b - 1].append([a - 1, c, d])

    def wait_time(d):
        tmp = INF; s = 0
        for t in range(max(0, int(d ** 0.5) - 2), int(d ** 0.5) + 3):
            if t + int(d / (t + 1)) < tmp:
                tmp = t + int(d  / (t + 1))
                s = t
        return s

    #ダイクストラ法
    def dijkstra_heap(s, n):
        dist = [INF] * n
        dist[s] = 0

        #(d[v], v)のペアを要素としたヒープを作る
        hq = [(dist[s], s)]

        while hq:
            #v:使用済みでない頂点のうち、d[v]が最小の頂点
            #d:vに対するキー値
            c, v = heappop(hq)
            #print(c, v)
            if dist[v] < c:
                continue
            for to, cost, d in g[v]:
                t = max(wait_time(d), dist[v])
                if t + cost + int(d / (t + 1)) < dist[to]:
                    dist[to] = t + cost + int(d / (t + 1))
                    heappush(hq, (dist[to], to))
            #print(dist)
        return dist

    dist = dijkstra_heap(0, n)
    #print(dist)
    if dist[n - 1] < INF:
        print(dist[n - 1])
    else:
        print(-1)

if __name__ == '__main__':
    main()
