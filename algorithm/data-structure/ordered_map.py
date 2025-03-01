from collections import OrderedDict


class OrderedMap:
    def __init__(self):
        self.data = OrderedDict()

    def insert(self, key, value):  # O(NlogN)
        self.data[key] = value
        self._sort()

    def erase(self, key):  # O(1)
        if key in self.data:
            del self.data[key]

    def find(self, key):  # O(1)
        return self.data.get(key, None)

    def size(self):  # O(1)
        return len(self.data)

    def empty(self):  # O(1)
        return len(self.data) == 0

    def begin(self):  # O(1)
        return next(iter(self.data.items()), None)

    def end(self):  # O(1)
        return next(reversed(self.data.items()), None)

    def show(self):  # O(N)
        return list(self.data.items())

    def _sort(self):  # O(NlogN)
        self.data = OrderedDict(sorted(self.data.items()))


# **デバッグ用の実行例**
print("=== Map 操作のデバッグ ===")

m = OrderedMap()

print("初期状態:", m.show())

m.insert(3, "three")
print("insert(3, 'three') ->", m.show())

m.insert(1, "one")
print("insert(1, 'one') ->", m.show())

m.insert(2, "two")
print("insert(2, 'two') ->", m.show())

print("find(2) ->", m.find(2))  # "two"
print("find(4) ->", m.find(4))  # None

print("size() ->", m.size())

print("begin() ->", m.begin())  # (1, "one")
print("end() ->", m.end())  # (3, "three")

m.erase(2)
print("erase(2) ->", m.show())

print("empty() ->", m.empty())

m.erase(1)
m.erase(3)
print("erase(1), erase(3) ->", m.show())

print("empty() ->", m.empty())
