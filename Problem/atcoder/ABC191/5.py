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
    reverse_g = [[] for _ in range(n)]
    for i in range(m):
        a, b, c = int_map()
        g[a - 1].append([b - 1, c])
        reverse_g[b - 1].append([a - 1, c])
    #print(g)
    #print(reverse_g)

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
            if dist[v] < c:
                continue
            for to, cost in g[v]:
                if dist[v] + cost < dist[to]:
                    dist[to] = dist[v] + cost
                    heappush(hq, (dist[to], to))
        return dist

    for i in range(n):
        dist = dijkstra_heap(i, n)
        #print(dist)
        ans = []
        for node in reverse_g[i]:
            if len(node) == 0:
                continue
            From = node[0]; cost = node[1]
            ans.append(dist[From] + cost)
        if len(ans) == 0 or min(ans) >= INF:
            print(-1)
        else:
            print(min(ans))


if __name__ == '__main__':
    main()
