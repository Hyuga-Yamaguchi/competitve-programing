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
    n, W = int_map()
    weight = [None] * n; value = [None] * n
    for i in range(n):
        w_, v_ = int_map()
        weight[i] = w_; value[i] = v_

    dp = [[0] * (W + 1) for _ in range(n + 1)]
    prev_w = [[None] * (W + 1) for _ in range(n + 1)]

    for i in range(n):
        for w in range(W + 1):
            #i番目の品物を選ぶ場合
            if w >= weight[i]:
                if dp[i + 1][w] < dp[i][w - weight[i]] + value[i]:
                    dp[i + 1][w] = dp[i][w - weight[i]] + value[i]
                    prev_w[i + 1][w] = w - weight[i]

            #i番目の品物を選ばない場合
            if dp[i + 1][w] < dp[i][w]:
                dp[i + 1][w] = dp[i][w]
                prev_w[i + 1][w] = w

    print(dp)
    print(dp[-1][-1])
    print(prev_w)
    for i in range(n + 1):
        for j in range(W + 1):
            print("|" + str(prev_w[i][j]), end = "")
        print("|")

    #復元
    print('Selected items are ...')
    cur_w = W
    for i in range(n - 1, -1, -1):
        #選んでいた場合
        if prev_w[i + 1][cur_w] == cur_w - weight[i]:
            print(i, 'th item (weight = ', weight[i], ', value = ', value[i], ')')

        #復元Tbをたどる
        cur_w = prev_w[i + 1][cur_w]


if __name__ == '__main__':
    main()

'''sample
6 8
2 3
1 2
3 6
2 1
1 3
5 85
'''
