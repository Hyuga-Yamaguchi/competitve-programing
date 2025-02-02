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
lower_start = 97 #"a"のASCIIコード
upper_start = 65 #"A"のASCIIコード
number_start = 48 #"0"のASCIIコード

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n, m = int_map()
    h = int_list()
    w = int_list()
    h.sort()
    w.sort()

    h_ = [None] * n
    for i in range(n):
        if i % 2 == 0:
            h_[i] = -h[i]
        else:
            h_[i] = h[i]
    #print(h_)

    cumsum_h = [None] * n
    cumsum_h[0] = h_[0]
    for i in range(1, n):
        cumsum_h[i] = cumsum_h[i - 1] + h_[i]
    #print(cumsum_h)

    ans = INF
    for i in range(m):
        index = bisect_right(h, w[i])
        #print(w[i], index)
        if index == 0:
            cur = -w[i] + cumsum_h[n - 1] * (-1)
        elif index % 2 == 1:
            cur = cumsum_h[index - 1] + w[i] + (cumsum_h[n - 1] - cumsum_h[index - 1]) * (-1)
        else:
            cur = cumsum_h[index - 1] - w[i] + (cumsum_h[n - 1] - cumsum_h[index - 1]) * (-1)
        #print(cur)

        ans = min(ans, cur)
    print(ans)



if __name__ == '__main__':
    main()
