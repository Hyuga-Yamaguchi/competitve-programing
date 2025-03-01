import math
from collections import Counter, deque
import itertools

INF = 1 << 60
MOD1 = 10**9 + 7


def int_input():
    return int(input())


def int_list(dec=False, to_tuple=False):
    result = [int(x) - dec for x in input().split()]
    return tuple(result) if to_tuple else result


def int_row(n, dec=False):
    return [int_input() - dec for _ in range(n)]


def int_row_list(n, dec=False, to_set=False):
    return (
        {int_list(dec, to_tuple=True) for _ in range(n)}
        if to_set
        else [int_list(dec) for _ in range(n)]
    )


def str_input():
    return input()


def str_list(to_tuple=False):
    result = list(input().split())
    return tuple(result) if to_tuple else result


def str_row(n):
    return [str_input() for _ in range(n)]


def str_row_list(n):
    return [str_list() for _ in range(n)]


def grid_input(h):
    return [list(input().strip()) for _ in range(h)]


def query_input(n, case_arg_types):
    """
    n: Number of queries
    case_arg_types: Args types list for case number
    """
    queries = []
    for _ in range(n):
        parts = input().split()
        case_num = parts[0]

        arg_types = case_arg_types.get(case_num, [])
        args = [arg_type(value) for arg_type, value in zip(arg_types, parts[1:])]

        queries.append((case_num, args))

    return queries


def string_join(sep, arr):
    return sep.join(map(str, arr))


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

    def lower_bound(self, value):
        if not self.ordered:
            return None
        idx = bisect.bisect_left(self.data, value)
        return self.data[idx] if idx < len(self.data) else None

    def upper_bound(self, value):
        if not self.ordered:
            return None
        idx = bisect.bisect_right(self.data, value)
        return self.data[idx] if idx < len(self.data) else None

    def show(self):  # us: O(N), os: O(N)
        return list(self.data)


def main():
    q = int_input()
    queries = query_input(q, {"1": [int], "2": [int], "3": [int]})

    desk = Set(ordered=True)
    ans = []
    for case, args in queries:
        val = args[0]
        if case == "1":
            desk.insert(val)
        elif case == "2":
            desk.erase(val)
        else:
            lb = desk.lower_bound(val)
            ans.append(lb if lb else -1)

    return string_join("\n", ans)


if __name__ == "__main__":
    print(main())
