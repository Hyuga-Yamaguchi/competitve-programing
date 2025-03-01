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


class UnorderedMap:
    def __init__(self):
        self.data = {}

    def insert(self, key, value):
        self.data[key] = value

    def erase(self, key):
        if key in self.data:
            del self.data[key]

    def find(self, key):
        return self.data.get(key, None)

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

    def show(self):
        return list(self.data.items())


def main():
    q = int_input()
    queries = query_input(q, {"1": [str, int], "2": [str]})

    scores = UnorderedMap()
    ans = []

    for case, args in queries:
        if case == "1":
            name, score = args
            scores.insert(name, score)
        else:
            name = args[0]
            ans.append(scores.find(name))

    return string_join("\n", ans)


if __name__ == "__main__":
    print(main())
