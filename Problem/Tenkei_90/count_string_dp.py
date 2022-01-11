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
    s = str_input()
    n = len(s)

    #res[i][c] := i文字目で最初に文字cが登場するindex(存在しないときはn)
    res = [[n] * 26 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        c = ord(s[i])
        for j in range(26):
            res[i][j] = res[i + 1][j]
        res[i][c - 97] = i
    for i in range(len(res)):
        print(i, *res[i], sep = "|")

    #DP
    dp = [0] * (n + 1)
    dp[0] = 1 #初期値->空文字列に対応
    for i in range(n):
        for j in range(26):
            if res[i][j] >= n:
                continue #次の文字jがもうない場合はスルー
            dp[res[i][j] + 1] += dp[i]
            dp[res[i][j] + 1] %= MOD
        print(i, *dp, sep="|")
    print(dp)

    ans = 0
    for i in range(n + 1):
        ans += dp[i]
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()
