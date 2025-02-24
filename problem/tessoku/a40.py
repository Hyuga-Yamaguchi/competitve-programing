import math
import collections

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


def factorial(n, m):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % m
    return result


def combination(n, r, m):
    if r < 0 or r > n:
        return 0

    num = factorial(n, m)
    den = factorial(r, m) * factorial(n - r, m) % m

    return num * pow(den, -1, m) % m


def main():
    n = int_input()
    lines_freq = collections.Counter(int_list()).values()

    return sum([combination(x, 3, MOD1) for x in lines_freq])


if __name__ == "__main__":
    print(main())
