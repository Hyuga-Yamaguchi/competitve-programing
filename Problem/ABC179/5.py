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
    n, x, m = int_map()
    y = copy(x)

    u = [0] * m
    u[y] += 1
    for i in range(3 * m):
        y = (y ** 2) % m
        u[y] += 1

    cycle = 0
    cycle_num = 0
    initial = 0
    initial_num = 0
    for i in range(m):
        if u[i] >= 2:
            cycle += i
            cycle_num += 1
        if u[i] == 1:
            initial += i
            initial_num += 1
    #print(cycle, cycle_num, initial, initial_num)

    z = copy(x)
    ini_lis = []
    cyc_lis = []
    for i in range(initial_num + cycle_num):
        if i == 0:
            if initial_num == 0:
                cyc_lis.append(z)
            else:
                ini_lis.append(z)
        elif i < initial_num:
            z = (z ** 2) % m
            ini_lis.append(z)
        else:
            z = (z ** 2) % m
            cyc_lis.append(z)
    #print(ini_lis, cyc_lis)

    if n <= initial_num:
        ans = 0
        for i in range(n):
            ans += ini_lis[i]
    elif n <= cycle_num:
        ans = initial
        for i in range(n - initial_num):
            ans += cyc_lis[i]
    else:
        div = (n - initial_num) // cycle_num
        rest = (n - initial_num) % cycle_num
        ans = initial + div * cycle
        for i in range(rest):
            ans += cyc_lis[i]
    print(ans)

if __name__ == '__main__':
    main()
