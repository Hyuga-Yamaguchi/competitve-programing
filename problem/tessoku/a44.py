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


def main():
    n, q = int_list()
    queries = int_row_list(q)

    a = list(range(1, n + 1))
    order = True
    ans = []

    for query in queries:
        if not query:
            continue

        w, *rest = query
        x, y = (rest + [None, None])[:2]
        if x is not None:
            x -= 1
            idx = x if order else n - 1 - x

        if w == 1:
            a[idx] = y
        elif w == 2:
            order = not order
        else:
            ans.append(a[idx])

    return string_join("\n", ans)


if __name__ == "__main__":
    print(main())
