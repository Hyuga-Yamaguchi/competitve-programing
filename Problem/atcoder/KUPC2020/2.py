import sys
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
u = list(list(map(int, input().split())) for _ in range(n))
e = 10 * 9 + 7

def dfs()
