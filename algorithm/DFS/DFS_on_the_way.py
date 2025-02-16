def dfs(G, v):
    #行きがけ順をインクリメントしながらメモ
    global first_ptr #参照渡しにするためglobal変数で定義
    first_order[v] = first_ptr
    first_ptr += 1

    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v)

    #帰りがけ順をインクリメントしながらメモ
    global last_ptr #参照渡しにするためglobal変数で定義
    last_order[v] = last_ptr
    last_ptr += 1

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
print(G)

#頂点を0とした時の探索
seen = [False] * n
first_order = [None] * n #行きがけ順
last_order = [None] * n #帰りがけ順

first_ptr = 0; last_ptr = 0
dfs(G, 0)

for v in range(n):
    print(str(v) + ": " + str(first_order[v]) + ", " + str(last_order[v]))

"""
"Sample"
15 14
0 1
1 2
1 3
0 4
4 5
5 6
5 7
4 8
8 9
8 10
0 11
11 12
11 13
13 14
"""
