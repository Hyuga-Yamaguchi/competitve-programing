"""
深さ優先探索の基本的な考え方
 基本的な考え方
  ・今いるところから隣に行こうとしてみる
  ・まだ行ってなかったらいく

 ちゃんと塗りつぶすために
  ・全箇所から４方向への移動を試し尽くす
  ・そのために、試し尽くしていない場所を覚えておき、戻ってくる

再帰関数による深さ優先探索
 考え方
  ・位置を引数にした再帰関数を使う
  ・自分から４方向への呼び出しを行う

 なぜこれで深さ優先探索になるのか？
  ・再帰関数なので呼び出した後戻ってくる
  ・戻ってきて違う方向へまたよびだす
"""


import sys
#再帰関数の呼び出し制限
sys.setrecursionlimit(10 ** 7)
h, w = map(int, input().split())
c = list(list(input()) for _ in range(h))

print(h, w, c)

def dfs(x, y):
    #壁に当たったり、探索範囲圏外になった場合はreturn
    if not (0 <= x < h) or not (0 <= y < w) or c[x][y] == "#":
        return
    #ゴールを見つけたら"Yes"を出力
    if c[x][y] == "g":
        print("Yes")
        sys.exit()

    #探索済のためのマーキング
    #再帰関数なので、１つの方向を試し終わった後、帰ってきて次の方向を試す
    #→全ての位置から４方向を試し尽くせる
    c[x][y] = "#"
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

#関数dfsをスタートの座標から呼び出す
for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            #スタート位置
            sx, sy = i, j
dfs(sx ,sy)
print("No")
