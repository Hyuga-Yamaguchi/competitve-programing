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
import numpy as np
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
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    s = str_input()
    s = s[:-1]
    tmp = 0; tmp_str = ""
    u = [0] * len(s)
    for i in range(2, len(s)):
        if s[i - 2] == s[i - 1] and s[i - 1] != s[i]:
            if tmp_str == s[i - 2]:
                tmp_str = s[i - 2]
            else:
                tmp_str = s[i - 2]
                tmp += 1
        if s[i] != tmp_str:
            u[i] += tmp
        else:
            u[i] += tmp - 1
    #print(u)
    print(sum(u))

if __name__ == '__main__':
    main()
