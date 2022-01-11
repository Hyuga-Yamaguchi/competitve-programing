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
    k = int_input()
    queen = [None] * k
    for i in range(k):
        a, b = int_map()
        queen[i] = [a, b]
    for v in permutations(range(8)):
        flag = True
        for [y, x] in queen:
            if v[x] != y:
                flag = False
        if flag:
            pos = []
            for i in v:
                pos.append([v[i], i])
            hantei = True
            for i in range(len(pos)):
                for j in range(i + 1, len(pos)):
                    if abs(pos[i][0] - pos[j][0]) == abs(pos[i][1] - pos[j][1]):
                        hantei = False
            if hantei:
                board = [["."] * 8 for _ in range(8)]
                #print(pos)
                for [y, x] in pos:
                    board[y][x] = "Q"
                for i in range(8):
                    t = ""
                    for j in range(8):
                        t += board[i][j]
                    print(t)
                exit()

if __name__ == '__main__':
    main()
