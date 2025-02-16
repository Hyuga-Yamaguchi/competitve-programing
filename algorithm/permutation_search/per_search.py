import itertools

for i in itertools.permutations(range("数列の最初の数","数列の最後の数")):
    lis = list(i); """リスト化""" #lis.insert(0, 1); lis.append(1)

    for j in range(n):
        """生成した各順列に対する処理"""


"""
組み合わせ combination
５枚のカード[0,4]から３枚引いた時に取れるカードの組み合わせ
昇順に並べる
tuple列を生成　listじゃないので注意！
"""
import itertools
list(itertools.combinations(range(5), 3))

"""
順列 permutation
4枚のカード[0,3]の並び順
昇順に並べる
tuple列を生成　listじゃないので注意！
"""
import itertools
list(itertools.permutations(range(4)))

"""
直積　product
複数リストの全パターン網羅
tuple列を生成　listじゃないので注意！
"""
import itertools
a = ["w1", "w2", "w3"]
b = ["s1", "s2", "s3", "s4"]
c = ["a1", "a2"]
list(itertools.product(a, b, c))

#出力結果
[('w1', 's1', 'a1'), ('w1', 's1', 'a2'), ('w1', 's2', 'a1'),
...
, ('w3', 's4', 'a2')]
