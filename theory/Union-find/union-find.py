from collections import defaultdict

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

"""class:UnionFindの使いかた"""
"""要素6個で初期化。初めは全ての要素が根となり別々のグループとなる"""
uf = UnionFind(6)
print("UnionFind(6)")
print("uf.parents = " + str(uf.parents))
print(uf)

"""union()でクループ併合"""
uf.union(0, 2)
print("uf.union(0, 2)")
print("uf.parents = " + str(uf.parents))
print(uf)

uf.union(1, 3)
print("uf.union(1, 3)")
print("uf.parents = " + str(uf.parents))
print(uf)

uf.union(4, 5)
print("uf.union(4, 5)")
print("uf.parents = " + str(uf.parents))
print(uf)

uf.union(1, 4)
print("uf.union(1, 4)")
print("uf.parents = " + str(uf.parents))
print(uf)

"""find()で要素の根を見つける"""
print("uf.find(0) = " + str(uf.find(0)))
print("uf.find(5) = " + str(uf.find(5)))

"""sizeで木の要素数を出力"""
print("uf.size(0) = " + str(uf.size(0)))
