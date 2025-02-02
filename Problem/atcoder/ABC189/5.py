import numpy as np
import sys
input = sys.stdin.readline

n = int(input())
xy = [None] * n
for i in range(n):
    xy[i] = np.array(list(map(int, input().split())) + [1], dtype = int).T

mat = [np.array([[0, 1, 0],[-1, 0, 0],[0, 0, 1]]),
np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]]),
np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])]

m = int(input())
lis = [None] * (m + 1); lis[0] = np.eye(3, dtype = int)
for i in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1: #-1/2 * pi 回転
        arr = mat[0]
    elif op[0] == 2: #1/2 * pi回転
        arr = mat[1]
    elif op[0] == 3: #x = p について対称移動
        mat[2][0, 2] = op[1] * 2; arr = mat[2]
    elif op[0] == 4: #y = pについての対称移動
        mat[3][1, 2] = op[1] * 2; arr = mat[3]
    lis[i + 1] = arr @ lis[i]

q = int(input())
for _ in range(q):
    A, B = map(int, input().split())
    ans = lis[A] @ xy[B - 1]
    print(ans[0], ans[1])
