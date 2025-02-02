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
    n, d = int_map()
    N = max(n, d)

    exp = [1] * (N + 1)
    for i in range(N):
        exp[i + 1] = exp[i] * 2
        exp[i + 1] %= mod

    ans = 0
    for depth in range(n):

        ## v == i or v == j
        if depth + d <= n - 1:
            ans += exp[d] * exp[depth]

        ## other
        l = max(1, depth + d - n + 1)
        r = min(d - 1, n - depth - 1)
        if r - l + 1 >= 0:
            ans += exp[d - 2] * (r - l + 1) * exp[depth]

        ans %= mod

    print((2 * ans) % mod)


if __name__ == '__main__':
    main()
