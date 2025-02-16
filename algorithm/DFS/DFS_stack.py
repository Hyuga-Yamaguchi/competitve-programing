"""
深さ優先探索の基本的な考え方
 基本的な考え方
  ・今いるところから隣に行こうとしてみる
  ・まだ行ってなかったらいく
 ちゃんと塗りつぶすために
  ・全箇所から４方向への移動を試し尽くす
  ・そのために、試し尽くしていない場所を覚えておき、戻ってくる

考え方
 ・試すべき位置をスタックで管理
 ・再帰呼び出しの代わりに、スタックでpush

アルゴリズム
 ・最初はスタート地点をスタックに投入
 ・繰り返す：スタックから位置を取り出して、まだ訪れていない隣があればpush
"""

import sys
h, w = map(int, input().split())
c = list(list(input()) for _ in range(h))

for i in range(h):
    for j in range(w):
        #スタート地点を探索
        if c[i][j] == "s":
            sx, sy = i, j
        #ゴール地点を探索
        elif c[i][j] == "g":
            gx, gy = i, j

#スタート地点をスタックに投入
stack = [[sx, sy]]
visited = [[0 for i in range(w)] for j in range(h)]
visited[sx][sy] = 1

dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while stack:
    #スタックの要素を取り出す
    x, y = stack.pop()
    for i in range(4):
        #現在の位置
        nx, ny = x + dx_dy[i][0], y + dx_dy[i][1]
        #壁に当たったり、探索範囲圏外になった場合はこれ以上進まない
        if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and c[nx][ny] != "#":
            #訪れた印をつける
            visited[nx][ny] = 1
            #スタック現在位置をpush
            stack.append([nx, ny])
            print("nx, ny = " + str([nx, ny]))
            print("stack = " + str(stack))
            print("visited = " + str(visited))
            print("--------------------------")
        if visited[gx][gy] == 1:
            print("Yes")
            sys.exit()

print("No")
