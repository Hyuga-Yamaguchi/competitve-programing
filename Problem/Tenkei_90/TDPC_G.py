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
    k = int_input()

    n = len(s)

    dp = [[0] * 26 for _ in range(n + 1)]

    dp[n - 1][ord(s[n - 1]) - ord("a")] = 1
    for i in range(n - 2, -1, -1):
        for c in range(26):
            if c != ord(s[i]) - ord("a"):
                dp[i][c] += dp[i + 1][c]
            else:
                dp[i][c] += 1 #cを採用した後は何も採用しないケース
                for c2 in range(26):
                    dp[i][c] += dp[i + 1][c2]

    cur = 0
    for c in range(26):
        cur += dp[0][c]
    #print(cur)

    #print(dp)
    if cur < k:
        print("Eel")
    else:
        res = ""; idx = 0
        while idx <= n - 1:
            #次の文字が何かを決める
            for j in range(26):
                if k - dp[idx][j] <= 0:
                    break
                k -= dp[idx][j]
            c = ord("a") + j #次の文字はc
            res += chr(c)
            #print(res)
            k -= 1 #cをとって終了し、残りは何もとらないような文字列を除外
            if k <= 0:
                break
            while s[idx] != chr(c):
                idx += 1
            idx += 1
            #print("idx", idx)
        print(res)

if __name__ == '__main__':
    main()
