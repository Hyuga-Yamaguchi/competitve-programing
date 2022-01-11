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
    g = [[] * n for _ in range(n)]
    for i in range(m):
        a, b = int_map()
        a -= 1; b -= 1
        g[a].append(b)
        g[b].append(a)
    #print(g)

    ans = 0
    for v in permutations(range(1, n)):
        v = [0] + list(v)
        #print(v)
        cnt = 0
        for i in range(len(v) - 1):
            if not v[i + 1] in g[v[i]]:
                continue
            cnt += 1
        if cnt == n - 1:
            ans += 1
    print(ans)



if __name__ == '__main__':
    main()
