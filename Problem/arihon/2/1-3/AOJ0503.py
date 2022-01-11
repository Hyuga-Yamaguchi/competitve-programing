import sys, re
# from math import ceil, floor, sqrt, pi, factorial, gcd
# from copy import copy, deepcopy
from collections import Counter, deque
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, product, combinations, combinations_with_replacement
# from bisect import bisect, bisect_left, bisect_right
# from functools import reduce
# from decimal import Decimal, getcontext
# from operator import itemgetter
#import numpy as np #pypyでは使用不可
input = sys.stdin.readline
def int_input(): return int(input())
def int_map(): return map(int, input().split())
# def int_list(): return list(int_map())
# def int_row(N): return [int_input() for _ in range(N)]
# def int_row_list(N): return [int_list() for _ in range(N)]
# def str_input(): return input()[:-1]
# def str_map(): return input().split()
# def str_list(): return list(str_map())
# def str_row(N): return [str_input() for _ in range(N)]
# def str_row_list(N): return [list(str_input()) for _ in range(N)]
# def lcm(a, b): return a * b // gcd(a, b)
# sys.setrecursionlimit(10 ** 9)
# INF = 1 << 60
# MOD = 10 ** 9 + 7
# mod = 998244353

#メモリ消費を抑える時はグローバル空間に書く
while True:
    n, m = int_map()
    if (n, m) == (0, 0):
        break
    a = [0]; b = [0]; c = [0]

    a += [int(i) for i in input().split()][1:]
    b += [int(i) for i in input().split()][1:]
    c += [int(i) for i in input().split()][1:]
    #print(a, b, c)

    q = deque()
    q.appendleft([a, b, c, 0, -1])
    tmp = [i for i in range(0, n + 1)]

    while q:
        a, b, c, d, t = q.pop()
        print(a, b, c, d, t)
        if d > m:
            print(-1)
            break
        if a == tmp or c == tmp:
            print(d)
            break

        if a[-1] > b[-1] and t != 1 and t != 0:
            q.appendleft([a[:-1], b + [a[-1]], c, d + 1, 0])
        if b[-1] > a[-1] and t != 0 and t != 1:
            q.appendleft([a + [b[-1]], b[:-1], c, d + 1, 1])
        if b[-1] > c[-1] and t != 3 and t != 2:
            q.appendleft([a, b[:-1], c + [b[-1]], d + 1, 2])
        if c[-1] > b[-1] and t != 2 and t != 3:
            q.appendleft([a, b + [c[-1]], c[:-1], d + 1, 3])
