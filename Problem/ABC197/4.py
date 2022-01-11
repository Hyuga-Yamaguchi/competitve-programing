import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd, cos, sin
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
INF = 1 << 60
MOD = 10 ** 9 + 7
mod = 998244353

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n = int_input()
    x0, y0 = int_map()
    xn, yn = int_map()

    X, Y = Decimal(str((x0 + xn) / 2)), Decimal(str((y0 + yn) / 2))
    #print(X, Y)
    new_x0 = Decimal(str(x0 - X)); new_y0 = Decimal(str(y0 - Y))
    #print(new_x0, new_y0)

    x1 = Decimal(str(Decimal(str(cos(2 * pi / n))) * new_x0 - Decimal(str(sin(2 * pi / n))) * new_y0))
    y1 = Decimal(str(Decimal(str(sin(2 * pi / n))) * new_x0 + Decimal(str(cos(2 * pi / n))) * new_y0))

    x1 += X; y1 += Y
    print(x1, y1)

if __name__ == '__main__':
    main()
