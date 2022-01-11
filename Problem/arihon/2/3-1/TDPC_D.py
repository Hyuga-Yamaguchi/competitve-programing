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

def prime_factorization(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n, d = int_map()

    fac = prime_factorization(d)
    u = defaultdict(int)

    if d == 1:
        print(1)
        exit()

    for num in fac:
        u[num] += 1
    #print(u)

    flag = True
    for key in u:
        if key != 2 and key != 3 and key != 5:
            flag = False

    if not flag:
        print(0)
        exit()

    i_max = u[2]; j_max = u[3]; k_max = u[5]
    #print(i_max, j_max, k_max)

    dp = [[[[0.0 for _ in range(k_max + 2)] for _ in range(j_max + 2)] for _ in range(i_max + 2)] for _ in range(n + 1)]
    dp[0][0][0][0] = 1.0


    for idx in range(n):
        for i in range(i_max + 1):
            for j in range(j_max + 1):
                for k in range(k_max + 1):
                    dp[idx + 1][i][j][k] += dp[idx][i][j][k] * (1 / 6)
                    dp[idx + 1][min(i_max, i + 1)][j][k] += dp[idx][i][j][k] * (1 / 6)
                    dp[idx + 1][i][min(j_max, j + 1)][k] += dp[idx][i][j][k] * (1 / 6)
                    dp[idx + 1][min(i_max, i + 2)][j][k] += dp[idx][i][j][k] * (1 / 6)
                    dp[idx + 1][i][j][min(k_max, k + 1)] += dp[idx][i][j][k] * (1 / 6)
                    dp[idx + 1][min(i + 1, i_max)][min(j_max, j + 1)][k] += dp[idx][i][j][k] * (1 / 6)
    #print(dp)
    print(dp[n][i_max][j_max][k_max])

if __name__ == '__main__':
    main()
