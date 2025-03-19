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


class RollingHash:
    def __init__(self, s, b=31, m=10**9 + 7):
        self.n = len(s)
        self.b = b
        self.m = m
        self.prefix_hash = [0] * (self.n + 1)
        self.power = [1] * (self.n + 1)

        for i in range(self.n):
            self.prefix_hash[i + 1] = (self.prefix_hash[i] * b + ord(s[i])) % m
            self.power[i + 1] = (self.power[i] * b) % m

        print(self.prefix_hash)
        print(self.power)

    def get_hash(self, l, r):
        hash_value = (
            self.prefix_hash[r] - self.prefix_hash[l] * self.power[r - 1]
        ) % self.m
        return hash_value if hash_value >= 0 else hash_value + self.m


def main():
    n, q = int_list()
    s = str_input()
    queries = int_row_list(q, dec=True)

    rs = RollingHash(s)
    ans = []
    print(rs.get_hash(0, 3))
    print(rs.get_hash(4, 7))
    for l1, r1, l2, r2 in queries:
        if rs.get_hash(l1, r1 + 1) == rs.get_hash(l2, r2 + 1):
            ans.append("Yes")
        else:
            ans.append("No")

    return string_join("\n", ans)


if __name__ == "__main__":
    print(main())
