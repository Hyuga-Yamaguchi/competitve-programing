"""
グラフ探索の実装(DFS)
グラフgにおいて頂点sを始点とした探索を行う(スタックによる実装)
"""
from collections import deque

#頂点数nと辺数m
n, m = map(int, input().split())
s = int(input())

#グラフの入力
g = [[] for _ in range(m)]
#g[i]は各頂点iに対し、隣接している頂点をリスト化している
#有向グラフ
for i in range (m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

#グラフ探索のためのデータ構造
seen = [False] * n #全頂点を「未訪問(False)」に初期化する
todo = deque([])

#初期条件
seen[s] = True #sを探索済にする
todo.append(s) #todoはsのみを含む状態となる

#todoが空になるまで探索を行う
while len(todo) != 0:
    #todoから頂点を取り出す
    v = todo[-1]
    todo.pop()

    #vから辿れる頂点を全て調べる
    for x in g[v]:
        #すでに発見済みの頂点は探索しない
        if seen[x]:
            continue

        #新たな頂点xを探索済としてtodoに挿入
        seen[x] = True
        todo.append(x)

    print("seen = " + str(seen))
    print("todo = " + str(todo))
    for i in range(n):
        if seen[i]:
            if not i in todo:
                print("Done = " + str(i))
