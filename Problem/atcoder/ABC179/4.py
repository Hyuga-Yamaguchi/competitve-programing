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
flaot_INF = float('inf')
INF = 1 << 60
MOD = 998244353

def main():
    n, k = int_map()
    dp = [0] * n; sdp = [0] * (n + 1)
    dp[0] = 1; sdp[1] = 1
    L = [None] * k; R = [None] * k
    for i in range(k):
        l, r = int_map()
        L[i] = l; R[i] = r
    for i in range(1, n):
        for j in range(k):
            left = max(0, i - R[j])
            right = max(0, i - L[j] + 1)
            dp[i] += (sdp[right] - sdp[left]) % MOD
        print("dp = " + str(dp))
        sdp[i + 1] = (sdp[i] + dp[i]) % MOD
        print("sdp = " + str(sdp))
    print(dp[-1] % MOD)

if __name__ == '__main__':
    main()
