from collections import OrderedDict


class Map:
    def __init__(self, ordered=True):
        self.ordered = ordered
        self.data = OrderedDict() if self.ordered else {}

    def insert(self, key, value):  # O(NlogN)
        self.data[key] = value
        if self.ordered:
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
        if not self.ordered:
            return None
        return next(iter(self.data.items()), None)

    def end(self):  # O(1)
        if not self.ordered:
            return None
        return next(reversed(self.data.items()), None)

    def show(self):  # O(N)
        return list(self.data.items())

    def _sort(self):  # O(NlogN)
        if not self.ordered:
            return None
        self.data = OrderedDict(sorted(self.data.items()))


print("=== Map 操作のデバッグ ===")

# **Unordered Map（ハッシュマップ）**
unordered_map = Map(ordered=False)

print("\n--- Unordered Map ---")
print("初期状態:", unordered_map.show())

unordered_map.insert(3, "three")
unordered_map.insert(1, "one")
unordered_map.insert(2, "two")

print("要素追加後:", unordered_map.show())

print("find(2) ->", unordered_map.find(2))  # "two"
print("find(4) ->", unordered_map.find(4))  # None

unordered_map.erase(2)
print("erase(2) ->", unordered_map.show())

print("empty() ->", unordered_map.empty())

unordered_map.erase(1)
unordered_map.erase(3)
print("erase(1), erase(3) ->", unordered_map.show())

print("empty() ->", unordered_map.empty())


# **Ordered Map（順序付きマップ）**
ordered_map = Map(ordered=True)

print("\n--- Ordered Map ---")
print("初期状態:", ordered_map.show())

ordered_map.insert(3, "three")
ordered_map.insert(1, "one")
ordered_map.insert(2, "two")

print("要素追加後:", ordered_map.show())

print("begin() ->", ordered_map.begin())  # (1, "one")
print("end() ->", ordered_map.end())  # (3, "three")

ordered_map.erase(2)
print("erase(2) ->", ordered_map.show())

print("empty() ->", ordered_map.empty())

ordered_map.erase(1)
ordered_map.erase(3)
print("erase(1), erase(3) ->", ordered_map.show())

print("empty() ->", ordered_map.empty())
