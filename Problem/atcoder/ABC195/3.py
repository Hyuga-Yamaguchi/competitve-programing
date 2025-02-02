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
    n = int_input()
    l = len(str(n))
    cnt = 0
    for i in range(l + 1):
        if i <= 3:
            continue
        elif 4 <= i <= l - 1:
            cnt += (10 ** i - 10 ** (i - 1)) * ((i - 1) // 3)
            #print((10 ** i - 10 ** (i - 1)) * ((i - 1) // 3))
        elif i == l:
            cnt += (n - 10 ** (i - 1) + 1) * ((i - 1) // 3)
            #print((n - 10 ** (i - 1) + 1) * ((i - 1) // 3))
    print(cnt)


if __name__ == '__main__':
    main()
