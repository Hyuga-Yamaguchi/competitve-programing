from collections import deque

#入力：グラフgと、探索の始点s
#出力：sからの各頂点への最短路長を表す配列
def bfs(g, s):
    n = len(g) #頂点数
    dist = [-1] * n #全頂点を未訪問に初期化
    que = deque([])

    #初期条件(頂点sを初期頂点とする)
    dist[s] = 0
    que.append(s) #sをqueにpush

    #BFS開始(キューが空になるまで探索を行う)
    while len(que) > 0:
        v = que[0]
        que.popleft()

        #vから辿れる頂点を全て調べる
        for x in g[v]:
            #すでに探索済の頂点は探索しない
            if dist[x] != -1:
                continue
            #新たに辿れる頂点xについて距離情報を更新してキューに挿入
            dist[x] = dist[v] + 1
            que.append(x)
    return dist

n = int(input())
g = [[] for _ in range(n)]
for i in range(n):
    lis = list(map(int, input().split()))
    for j in range(2, len(lis)):
        g[lis[0] - 1].append(lis[j] - 1)

dist = bfs(g, 0)
for v in range(n):
    print(str(v + 1) + " " + str(dist[v]))
