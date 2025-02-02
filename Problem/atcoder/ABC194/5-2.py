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
    n, m = int_map()
    a = int_list()
    def mex_add(arr, in_int):
        if in_int - 1 in arr and in_int + 1 in arr:
            arr.discard(in_int - 1)
            arr.discard(in_int + 1)
        elif in_int - 1 in arr:
            arr.discard(in_int - 1)
            arr.add(in_int)
        elif in_int + 1 in arr:
            arr.discard(in_int + 1)
            arr.add(in_int)
        else:
            arr.add(in_int)

    def mex_discard(arr, out_int):
        max_int = max(arr)
        if out_int >= 1 and out_int != max_int:
            if out_int in arr:
                arr.discrd(out_int)
            else:
                arr.add(out_int + 1)
                arr.add(out_int - 1)
        elif out_int == 0:
            arr.discard(0)
            arr.add(1)
        elif out_int == max_int:
            arr.discard(max_int)
            arr.add(max_int - 1)

    #初期設定
    b = a[0:m]
    x = set([])
    for i in b:
        x.add(i)
    print(x)
    for i in range(n - m):
        if a[m + i] == a[i]:
            continue
        mex_add(x, a[m + i])
        mex_discard(x, a[i])
        print(x)
    x = list(x)
    if 0 in x:
        print(x[1] + 1)
    else:
        print(0)

if __name__ == '__main__':
    main()
