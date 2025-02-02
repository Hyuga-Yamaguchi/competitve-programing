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
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main():
    n, m, x, y = int_map()
    x -= 1; y -= 1
    g = [[] for _ in range(n)]
    for i in range(m):
        a, b, t, k = int_map()
        g[a - 1].append([b - 1, t, k])
        g[b - 1].append([a - 1, t, k])
    #print(g)

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
            for to, cost, start in g[v]:
                if ceil(dist[v] / start) * start + cost < dist[to]:
                    #print(ceil((dist[v] + cost) / start) * start)
                    dist[to] = ceil(dist[v] / start) * start + cost
                    heappush(hq, (dist[to], to))
        return dist

    dist = dijkstra_heap(x, n)
    if dist[y] < INF:
        print(dist[y])
    else:
        print(-1)

if __name__ == '__main__':
    main()
