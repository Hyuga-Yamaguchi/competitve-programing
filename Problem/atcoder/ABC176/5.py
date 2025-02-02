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
    h, w, m = int_map()
    H = [0] * h; W = [0] * w
    yx = set([])
    for i in range(m):
        y, x = int_map()
        H[y - 1] += 1
        W[x - 1] += 1
        yx.add((y - 1, x - 1))
    #print(yx)
    H_max = max(H); W_max = max(W)
    H_lis = set(); W_lis = set() #maxの候補
    for i in range(h):
        if H[i] == H_max:
            H_lis.add(i)
    for i in range(w):
        if W[i] == W_max:
            W_lis.add(i)
    #print(H_lis, W_lis)

    cnt = 0
    for i in yx:
        if i[0] in H_lis and i[1] in W_lis:
            cnt += 1
    if len(H_lis) * len(W_lis) == cnt:
        print(H_max + W_max - 1)
    else:
        print(H_max + W_max)


if __name__ == '__main__':
    main()
