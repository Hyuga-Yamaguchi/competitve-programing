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
    D, G = int_map()
    p = [None] * D; c = [None] * D
    for i in range(D):
        P, C = int_map()
        p[i] = P; c[i] = C

    ans = INF
    for bit in range(1 << D):
        s = 0; num = 0; rest_max = -1
        for i in range(D):
            if (bit >> i) & 1:
                s += 100 * (i + 1) * p[i] + c[i]
                num += p[i]
            else:
                rest_max = i
        if s < G:
            s1 = 100 * (rest_max + 1)
            incomplete = (G - s + s1 - 1) // s1
            if incomplete >= p[rest_max]:
                continue
            num += incomplete
        ans = min(ans, num)
    print(ans)





if __name__ == '__main__':
    main()
