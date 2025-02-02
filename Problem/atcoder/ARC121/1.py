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
    n = int_input()
    lis = []
    for i in range(n):
        x, y = int_map()
        lis.append((x, y, i))
    ids = set()
    for i in range(2):
        cand = sorted(lis, key = itemgetter(i))
        for j in range(2):
            ids.add(cand[j])
            ids.add(cand[- j - 1])
    #print(ids)

    index = set()
    for cri in ids:
        for j in range(n):
            if (cri[2], j) in index or (j, cri[2]) in index:
                continue
            index.add((cri[2], j))
    #print(index)

    ans = []
    for home in index:
        x0 = lis[home[0]][0]; y0 = lis[home[0]][1]
        x = lis[home[1]][0]; y = lis[home[1]][1]
        ans.append(max(abs(x0 - x), abs(y0 - y)))
    print(sorted(ans)[-2])


if __name__ == '__main__':
    main()
