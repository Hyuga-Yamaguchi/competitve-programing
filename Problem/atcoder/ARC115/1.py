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
    S = [None] * n
    for i in range(n):
        s = str_input()
        s_sum = 0
        for j in range(m):
            s_sum += int(s[j])
        S[i] = s_sum
    even_count = 0; odd_count = 0
    for i in range(n):
        if S[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    ans = n * (n - 1) // 2 - even_count * (even_count - 1) // 2 - odd_count * (odd_count - 1) // 2
    print(ans)


if __name__ == '__main__':
    main()
