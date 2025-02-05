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
    def xgcd(a, b):
        x0, y0, x1, y1 = 1, 0, 0, 1
        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return a, x0, y0

    def modinv(a, m):
        g, x, y = xgcd(a, m)
        if g != 1:
            return -1
        else:
            return x % m

    t = int_input()
    for case in range(t):
        x, y, p, q = int_map()
        ans = []
        for i in range(y):
            for j in range(q):
                a = 2 * (x + y); b = (p + q); c = (x + y) - q - i + j
                d = gcd(gcd(a, b), c)
                a //= d; b //= d; c //= d

                if gcd(a, b) != 1:
                    continue
                else:
                    ans.append(c * modinv(a, b) % b)
        print(ans)
        if ans:
            print(min(ans))
        else:
            print("infinity")




if __name__ == '__main__':
    main()
