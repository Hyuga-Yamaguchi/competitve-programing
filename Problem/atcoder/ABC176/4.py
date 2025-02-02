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
    h, w = int_map()
    ch, cw = int_map()
    ch -= 1; cw -= 1
    dh, dw = int_map()
    dh -= 1; dw -= 1
    S = [None] * h
    for i in range(h):
        s = str_input()
        S[i] = s
    #print(S)

    def bfs(sy, sx):
        queue = deque([[sy, sx]])
        cost[sy][sx] = 0
        #print(sy, sx)
        cnt = 0
        while queue:
            #print(queue)
            [y, x] = queue.popleft()
            cnt += 1
            #print([y, x])
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if not 0 <= ny < h or not 0 <= nx < w:
                    continue
                if S[ny][nx] == "#":
                    continue
                if cost[ny][nx] <= cost[y][x]:
                    continue
                cost[ny][nx] = cost[y][x]
                queue.appendleft((ny, nx))
            for dy in range(-2, 3):
                for dx in range(-2, 3):
                    ny, nx = y + dy, x + dx
                    if not 0 <= ny < h or not 0 <= nx < w:
                        continue
                    if S[ny][nx] == "#":
                        continue
                    if cost[ny][nx] <= cost[y][x] + 1:
                        continue
                    cost[ny][nx] = cost[y][x] + 1
                    queue.append((ny, nx))
        print(cnt)

    cost = [[INF] * w for _ in range(h)]
    bfs(ch, cw)
    #print(cost)
    print(cost[dh][dw] if cost[dh][dw] != INF else -1)

if __name__ == '__main__':
    main()
