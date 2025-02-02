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
float_INF = float('inf')
INF = 1 << 60
MOD = 10 ** 9 + 7

def main():
    n = int_input()
    C = [None] * n
    for i in range(n):
        c = int_list()
        C[i] = c
    sa = [[None] * (n - 1) for _ in range(n)]
    for i in range(n):
        for j in range(n - 1):
            sa[i][j] = C[i][j + 1] - C[i][j]
    #print(sa)
    flag = True
    for i in range(n - 1):
        if not sa[i] == sa[i + 1]:
            flag = False
    if flag:
        print("Yes")
        h_min = INF; min_index = 0
        for i in range(n):
            if h_min >= C[i][0]:
                h_min = C[i][0]
                min_index = i
        b = C[min_index]
        a = [None] * n
        for i in range(n):
            a[i] = C[i][0] - b[0]
        print(*a)
        print(*b)
    else:
        print("No")



if __name__ == '__main__':
    main()
