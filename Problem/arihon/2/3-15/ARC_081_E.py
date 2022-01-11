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
    a = str_input()
    n = len(a)

    res = [[n + 1] * 26 for _ in range(n + 2)]
    for i in range(n - 1, -1, -1):
        for j in range(26):
            res[i][j] = res[i + 1][j]
            res[i][ord(a[i]) - ord("a")] = i
    print(res)

    dp = [INF] * (n + 1)
    recon = ["a"] * (n + 1)
    dp[n] = 1
    for i in range(n - 1, -1, -1):
        for j in range(26):
            #次の文字がないとき
            if res[i][j] == n + 1:
                if dp[i] > 1:
                    dp[i] = 1
                    recon[i] = chr(ord("a") + j)
            #次の文字があるとき
            elif dp[i] > dp[res[i][j] + 1] + 1:
                print("flag")
                dp[i] = dp[res[i][j] + 1] + 1
                recon[i] = chr(ord("a") + j)
            print(i, dp, recon)
    print(dp)
    print(recon)

    ans = ""; idx = 0
    while idx <= n:
        ans += recon[idx]
        idx = res[idx][ord(recon[idx]) - ord("a")] + 1
    print(ans)

if __name__ == '__main__':
    main()
