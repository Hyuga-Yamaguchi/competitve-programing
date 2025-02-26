import math
from collections import Counter
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


def string_join(sep, arr):
    return sep.join(map(str, arr))


def calc_players(members, ba, bb, k):

    return sum(1 for a, b in members if ba <= a <= ba + k and bb <= b <= bb + k)


def main():
    n, k = int_list()
    members = int_row_list(n)

    unique_a = set(a for a, _ in members)
    unique_b = set(b for _, b in members)

    boundary = [[a, b] for a in unique_a for b in unique_b]

    return max(calc_players(members, a, b, k) for a, b in boundary)


if __name__ == "__main__":
    print(main())
