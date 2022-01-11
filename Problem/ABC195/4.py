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
MOD = 10 ** 9 + 7

def main():
    n, m, q = int_map()
    wv = [None] * n
    for i in range(n):
        WV = int_list()
        wv[i] = WV
    wv = sorted(wv, key = itemgetter(1), reverse = True)
    #print(wv)
    x = int_list()
    for i in range(q):
        l, r = int_map()
        y = x[:l - 1] + x[r:]
        for j in range(len(y)):
            y[j] = [y[j], True]
        y = sorted(y, key = itemgetter(0))
        #print(y)
        ans = 0
        for j in wv:
            for k in y:
                if not k[1]:
                    continue
                if j[0] <= k[0]:
                    ans += j[1]
                    k[1] = False
                    break
                #print(y)
        print(ans)

if __name__ == '__main__':
    main()
