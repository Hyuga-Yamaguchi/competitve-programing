"""有向グラフGの２頂点s, tが与えられた時、sから辺を辿ってtに到達できるかどうかを判定
sを始点としたDFSを実施　DFS実施後においてseen配列を見ることで,各頂点が探索されたかどうかを判定
"""
"""
StackによるDFSで実施
"""
"""
Sample
8 12
s t
4 1
4 2
4 6
1 6
1 3
6 7
2 7
2 5
7 0
3 7
3 0
0 5
"""
from collections import deque

#頂点数nと辺数m, 始点sと終点t
n, m = map(int, input().split())
s, t = map(int, input().split())

#グラフの入力
g = [[] for _ in range(m)]
#g[i]は各頂点iに対し、隣接している頂点をリスト化している
#有向グラフ
for i in range (m):
    a, b = map(int, input().split())
    g[a].append(b)

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

if seen[t]:
    print("Yes")
else:
    print("No")
