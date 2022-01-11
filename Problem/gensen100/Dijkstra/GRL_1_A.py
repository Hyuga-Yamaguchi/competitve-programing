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
    v, e, r = int_map()

    g = [[] for _ in range(v)]
    for i in range(e):
        s, t, d = int_map()
        g[s].append([t, d])

    #ダイクストラ法
    def dijkstra_heap(s, n):
        dist = [INF] * n
        dist[s] = 0

        #(d[v], v)のペアを要素としたヒープを作る
        hq = [(dist[s], s)]
        seen = [False] * n #ノードが確定済みかどうか

        while hq:
            #v:使用済みでない頂点のうち、d[v]が最小の頂点
            #d:vに対するキー値
            v = heappop(hq)[1]
            seen[v] = True
            for to, cost in g[v]:
                if seen[to] == False and dist[v] + cost < dist[to]:
                    dist[to] = dist[v] + cost
                    heappush(hq, (dist[to], to))
        return dist

    dist = dijkstra_heap(r, v)
    for i in range(len(dist)):
        if dist[i] < INF:
            print(dist[i])
        else:
            print("INF")

if __name__ == '__main__':
    main()
