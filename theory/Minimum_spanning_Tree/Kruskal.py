"""
最小全域木問題
連結な重み付き無向グラフG=(V, E)が与えられる。
Gの全域木Tの重みw(T)として考えられる最小値を求める
"""
"""
クラスカル法
辺集合Tを空集合とします
各辺を重みが小さい順にソートして,e[0], e[1],,,,e[M - 1]とする。
各i = 0, 1,,,,,M - 1に対して:
    Tに辺e[i]を追加した時に、サイクルが形成されるならば:
        辺e[i]を破棄する
    サイクルが形成されないならば,
        Tに辺e[i]を追加する
Tが求める最小全域木となる
"""
"""
Sample
8 12
0 3 5
0 5 6
0 7 3
1 3 8
1 4 4
1 6 3
2 4 9
2 5 10
2 7 5
3 7 6
4 6 2
6 7 7
"""
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        #各要素の親要素番号を格納するリスト　要素が根の場合は、-(そのグループの要素数)

    """要素xが属するグループの根を返す"""
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    """要素xが属するグループと要素yが属するグループとを併合する"""
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    """要素xが属するグループのサイズ（要素数）を返す"""
    def size(self, x):
        return -self.parents[self.find(x)]

    """要素x, yが同じグループに属するかどうかを返す"""
    def same(self, x, y):
        return self.find(x) == self.find(y)

    """要素xが属するグループに属する要素をリストで返す"""
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    """すべての根の要素をリストで返す"""
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    """グループの数を返す"""
    def group_count(self):
        return len(self.roots())

    """{ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す"""
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    """print()での表示用"""
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

n, m = map(int, input().split()) #頂点数と辺数
edge = [None] * m #辺集合
for i in range(m):
    a, b, w = map(int, input().split())
    edge[i] = [w, a, b]

#各辺を、辺の重みが小さい順にソートする
#pairはデフォルトで、(第一要素,第二要素)の辞書順比較
edge.sort()
print(edge)

#クラスカル法
res = 0
uf = UnionFind(n)
for i in range(m):
    w = edge[i][0]
    u = edge[i][1]
    v = edge[i][2]

    #辺(u, v)の追加によってサイクルを形成されるときは追加しない
    if uf.same(u, v):
        continue

    #辺(u, v)を追加する
    res += w
    uf.union(u, v)

print(res)
