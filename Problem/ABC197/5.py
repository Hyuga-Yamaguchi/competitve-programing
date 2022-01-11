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
#import numpy as np #pypyでは使用不可
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
INF = 1 << 100
MOD = 10 ** 9 + 7
mod = 998244353

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n = int_input()
    xc = [None] * n; max_c = 0
    for i in range(n):
        x, c = int_map()
        c -= 1
        max_c = max(max_c, c)
        xc[i] = [x, c]
    ##xc.sort(key = itemgetter(1))
    #print(xc, max_c)

    lr_sub = [[] for _ in range(max_c + 1)];
    for i in range(n):
        lr_sub[xc[i][1]].append(xc[i][0])

    lr = [[None] * 2 for _ in range(max_c + 1)]
    for i in range(max_c + 1):
        if len(lr_sub[i]) == 0:
            continue
        lr[i][0] = min(lr_sub[i])
        lr[i][1] = max(lr_sub[i])
    lr = [i for i in lr if i != [None, None]]
    #print(lr)

    l1 = 0; r1 = 0; lcst = 0; rcst = 0
    for i in range(len(lr)):
        l2 = lr[i][0]; r2 = lr[i][1]
        lcst2 = INF; rcst2 = INF

        #i回目のend_i+1回目のstart_i+1回目のend
        #l1 -> l2 -> r2
        rcst2 = min(rcst2, lcst + abs(l1 - l2) + abs(l2 - r2))
        #l1 -> r2 -> l2
        lcst2 = min(lcst2, lcst + abs(l1 - r2) + abs(r2 - l2))
        #r1 -> l2 -> r2
        rcst2 = min(rcst2, rcst + abs(r1 - l2) + abs(l2 - r2))
        #r1 -> r2 -> l2
        lcst2 = min(lcst2, rcst + abs(r1 - r2) + abs(r2 - l2))

        l1 = l2; r1 = r2; lcst = lcst2; rcst = rcst2
        print(l1, r1, lcst, rcst)
    ans = min(lcst + abs(l1), rcst + abs(r1))
    print(ans)

if __name__ == '__main__':
    main()
