import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd, log10
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
    d = int_input()
    n = int_input()
    m = str(n)
    digit = int(log10(n) + 1)
    #print(digit)

    dp = [[[0] * d for _ in range(2)] for _ in range(digit + 1)]
    dp[0][0][0] = 1

    for i in range(digit):
        for j in range(d):
            for k in range(10):
                dp[i + 1][1][(j + k) % d] += dp[i][1][j]
                dp[i + 1][1][(j + k) % d] %= MOD
                if 0 <= k <= int(m[i]) - 1:
                    dp[i + 1][1][(j + k) % d] += dp[i][0][j]
                    dp[i + 1][1][(j + k) % d] %= MOD
                if k == int(m[i]):
                    dp[i + 1][0][(j + int(m[i])) % d] = dp[i][0][j]
    print(dp[digit][0][0] + dp[digit][1][0] - 1)

if __name__ == '__main__':
    main()
