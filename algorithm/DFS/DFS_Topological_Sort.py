"""
トポロジカルソート:与えられた有向グラフに対し、各頂点を辺の向きに沿うように順序をつけて並び替える。
＊有向グラフGが有向サイクルを含まないことが必要十分条件(DAG)
＊トポロジカルソート順は一意でなく、複数通り存在する
＊再帰関数を使用した深さ優先探索をする
"""
"""
各頂点v ∈ Vについて
再帰関数dfs(G, v)が呼ばれる瞬間(行きがけ順)：v-in
再帰関数dfs(G, v)を終了する瞬間(帰りがけ順)：v-out
と表す
"""
"""
考え方
深さ優先探索における再帰関数を抜けた順序に頂点を並べ、それを逆順に並べる
→トポロジカルソート順が得られる
"""
#トポロジカルソートをする
def rec(g, v):
    seen[v] = True
    for next_v in g[v]:
        if seen[next_v]:
            continue
        rec(g, next_v)
    #v-outを記憶する
    order.append(v)

n, m = map(int, input().split()) #頂点数と枝数
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

#探索
seen = [False] * n
order = [] #トポロジカルソート順を表す
for v in range(n):
    if seen[v]:
        continue
    rec(g, v)
order.reverse()

for v in order:
    print(str(v) + " -> ", end = "")
print("")
