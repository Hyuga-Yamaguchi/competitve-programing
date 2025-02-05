import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
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
def str_input(): return input()[:-1]
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
    w, h = int_map()
    a = [[0] + list(map(int, input().split())) + [0] for _ in range(h)]
    a = [[0] * (w + 2)] + a + [[0] * (w + 2)]
    #print(a)

    cnt = 0
    q = deque()
    q.append([0, 0])
    a[0][0] = -1
    while q:
        [y, x] = q.popleft()
        if y % 2 == 0:
            direction = [(-1, -1), (0, -1), (1, -1), (1, 0), (0, 1), (-1, 0)]
        else:
            direction = [(-1, 0), (0, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        for (dy, dx) in direction:
            ny = y + dy; nx = x + dx
            if not 0 <= ny < h + 2 or not 0 <= nx < w + 2:
                continue
            if a[ny][nx] == 1:
                cnt += 1
            if a[ny][nx] == 0:
                a[ny][nx] = -1
                q.append([ny, nx])
        #print(a)
        #print(cnt)
    print(cnt)





if __name__ == '__main__':
    main()
