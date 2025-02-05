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
    n = int_input()
    s = str_input()

    dp = [[[0] * 11 for _ in range(1 << 11)] for _ in range(n + 1)]
    dp[0][0][10] = 1
    for i in range(n):
        for mask in range(1 << 11):
            for last in range(11):
                dp[i + 1][mask][last] += dp[i][mask][last] #出場しない場合
                dp[i + 1][mask][last] %= mod

                next = ord(s[i]) - ord('A')

                #コンテストに出場する時
                if (mask & (1 << next)) and last != next: #次に出るコンテストに以前出ていて、かつ最後と違う時
                    continue
                dp[i + 1][mask | (1 << next)][next] += dp[i][mask][last]
                dp[i + 1][mask | (1 << next)][next] %= mod

    #print(dp[n])
    ans = 0
    for i in range(1 << 11):
        for j in range(11):
            ans += dp[n][i][j]
            ans %= mod
    print(ans - 1)

if __name__ == '__main__':
    main()
