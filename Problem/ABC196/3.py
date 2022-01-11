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
    n = str_input()[:-1]
    l = len(n)
    if l % 2 == 1:
        l //= 2
        ans = 10 ** l - 1
    else:
        l //= 2
        ans = 10 ** (l - 1) - 1
        half_1 = int(n[0 : l])
        half_2 = int(n[l : 2 * l])
        #print(half_1, half_2)
        if half_1 <= half_2:
            ans += half_1 - 10 ** (l - 1) + 1
        else:
            ans += half_1 - 10 ** (l - 1)
    print(ans)

if __name__ == '__main__':
    main()
