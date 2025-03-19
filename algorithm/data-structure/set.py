from sortedcontainers import SortedSet
import bisect


class Set:
    def __init__(self, ordered=True):
        self.ordered = ordered
        self.data = SortedSet() if ordered else set()

    def insert(self, value):  # us: O(1), os: O(logN)
        self.data.add(value)

    def erase(self, value):  # us: O(1), os: O(logN)
        self.data.discard(value)

    def find(self, value):  # us: O(1), os: O(logN)
        return value in self.data

    def size(self):  # us: O(1), os: O(1)
        return len(self.data)

    def empty(self):  # us: O(1), os: O(1)
        return len(self.data) == 0

    def begin(self):  # us: -, os: O(1)
        return next(iter(self.data), None) if self.ordered else None

    def end(self):  # us: -, os: O(1)
        return next(reversed(self.data), None) if self.ordered else None

    def lower_bound(self, value):  # us: -, os: O(logN)
        if not self.ordered:
            return None
        idx = bisect.bisect_left(self.data, value)
        return self.data[idx] if idx < len(self.data) else None

    def upper_bound(self, value):  # us: -, os: O(logN)
        if not self.ordered:
            return None
        idx = bisect.bisect_right(self.data, value)
        return self.data[idx] if idx < len(self.data) else None

    def show(self):  # us: O(N), os: O(N)
        return list(self.data)


print("=== Set 操作のデバッグ ===")

# **順序なし（Unordered Set）**
unordered_set = Set(ordered=False)

print("\n--- Unordered Set ---")
print("初期状態:", unordered_set.show())

unordered_set.insert(10)
print("insert(10) ->", unordered_set.show())

unordered_set.insert(20)
print("insert(20) ->", unordered_set.show())

unordered_set.insert(10)  # 重複は無視
print("insert(10) (duplicate) ->", unordered_set.show())

print("find(20) ->", unordered_set.find(20))  # True
print("find(30) ->", unordered_set.find(30))  # False

print("size() ->", unordered_set.size())

unordered_set.erase(20)
print("erase(20) ->", unordered_set.show())

print("empty() ->", unordered_set.empty())

unordered_set.erase(10)
print("erase(10) ->", unordered_set.show())

print("empty() ->", unordered_set.empty())


# **順序あり（Ordered Set）**
ordered_set = Set(ordered=True)

print("\n--- Ordered Set ---")
print("初期状態:", ordered_set.show())

ordered_set.insert(10)
ordered_set.insert(20)
ordered_set.insert(30)
ordered_set.insert(40)
ordered_set.insert(50)

print("要素追加後:", ordered_set.show())

print("lower_bound(25) ->", ordered_set.lower_bound(25))  # 30
print("lower_bound(10) ->", ordered_set.lower_bound(10))  # 10
print("lower_bound(55) ->", ordered_set.lower_bound(55))  # None

print("upper_bound(25) ->", ordered_set.upper_bound(25))  # 30
print("upper_bound(30) ->", ordered_set.upper_bound(30))  # 40
print("upper_bound(50) ->", ordered_set.upper_bound(50))  # None
