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
#import numpy as np
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
    #ダイクストラ法
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

    n, k = int_map()
    g = [[] for _ in range(n)]
    for i in range(k):
        lis = int_list()
        if len(lis) == 3:
            flag = lis[0]; a = lis[1] - 1; b = lis[2] - 1
        elif len(lis) == 4:
            flag = lis[0]; c = lis[1] - 1; d = lis[2] - 1; e = lis[3]
        if flag == 0:
            dist = dijkstra_heap(a, n)
            if dist[b] < INF:
                print(dist[b])
            else:
                print(-1)
        elif flag == 1:
            g[c].append([d, e])
            g[d].append([c, e])

if __name__ == '__main__':
    main()
