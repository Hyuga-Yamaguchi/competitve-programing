import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from operator import itemgetter
#import numpy as np
input = sys.stdin.readline
def int_input(): return int(input())
def int_map(): return map(int, input().split())
def int_list(): return list(int_map())
def int_row(N): return [int_input() for _ in range(N)]
def int_row_list(N): return [int_list() for _ in range(N)]
def str_input(): return input()[:-1]
def str_map(): return input().split()
def str_list(): return list(str_map())
def str_row(N): return [str_input() for _ in range(N)]
def str_row_list(N): return [list(str_map()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 10 ** 9 + 7
mod = 998244353
lower_start = 97 #"a"のASCIIコード
upper_start = 65 #"A"のASCIIコード
number_start = 48 #"0"のASCIIコード

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n = int_input()
    s = str_row(n)
    t = str_row(n)
    print(s, t)

    s_list = list((i, j) for i in range(n) for j in range(n) if s[i][j] == "#")
    t_list = list((i, j) for i in range(n) for j in range(n) if t[i][j] == "#")

    print(s_list, t_list)

    if len(s_list) != len(t_list):
        print("No")
        exit()

    for _ in range(4):
        for i in range(- n + 1, n):
            for j in range(- n + 1, n):
                flag = True
                for x, y in s_list:
                    if not (0 <= x + i < n and 0 <= y + j < n and t[x + i][y + i] == "#"):
                        flag = False
                        break
                if flag:
                    print("Yes")
                    exit()
        s_list = [(y, n - 1 - x) for x, y in s_list]
    print("No")


if __name__ == '__main__':
    main()
