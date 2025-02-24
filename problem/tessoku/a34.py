import math

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


from functools import reduce
from operator import xor
import itertools


def nim_sum(arr):
    return reduce(xor, arr, 0)


def grundy_number(arr):
    s = set(arr)

    return next(i for i in itertools.count() if i not in s)


def calc_rocks_grundy(n, x, y):
    grundy = [0] * (n + 1)

    for i in range(n + 1):
        reachable_state = set()
        if i >= x:
            reachable_state.add(grundy[i - x])
        if i >= y:
            reachable_state.add(grundy[i - y])
        grundy[i] = next(g for g in itertools.count() if g not in reachable_state)

    return grundy


def main():
    n, x, y = int_list()
    rocks = int_list()

    rocks_grundy_nums = calc_rocks_grundy(max(rocks), x, y)

    return (
        "Second" if nim_sum(map(rocks_grundy_nums.__getitem__, rocks)) == 0 else "First"
    )


if __name__ == "__main__":
    print(main())
