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
    a = int_list()
    max_a = max(a)
    pos = [[0] for _ in range(max_a + 2)]
    for i in range(n):
        pos[a[i]].append(i + 1)
    for i in range(max_a + 2):
        pos[i].append(n + 1)
    #print(pos)
    ans = 0
    flag = False
    for i in range(max_a + 2):
        for j in range(len(pos[i]) - 1):
            if pos[i][j + 1] - pos[i][j] > m:
                ans = i
                flag = True
                break
        if flag:
            break
    print(ans)

if __name__ == '__main__':
    main()
