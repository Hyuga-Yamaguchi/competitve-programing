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
INF = 10 ** 20
MOD = 10 ** 9 + 7

def main():
    x = str_input()
    x = x[:-1]; #print(x)
    m = int_input()
    max_x = 0
    for i in range(len(x)):
        max_x = max(max_x, int(x[i]))
    #print(max_x)
    def base_n_to_10(X, n):
        out = 0
        for i in range(1, len(str(X)) + 1):
            out += int(X[-i]) * (n ** (i - 1))
        return out

    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
    else:
        max_x += 1;
        left = 0; right = INF
        while right - left > 1:
            mid = (left + right) // 2
            if base_n_to_10(x, mid) <= m:
                left = mid
            else:
                right = mid
        else:
            print(max(left - max_x + 1, 0))

if __name__ == '__main__':
    main()
