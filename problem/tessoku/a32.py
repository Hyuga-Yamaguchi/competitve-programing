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


def dp_table(n, a, b):
    """
    負けの状態になる条件
    - 負けの状態に遷移するような行動が存在しない場合
    - 取れる行動がない場合

    勝ちの状態になる条件
    - 負けの状態に遷移するような行動が存在する場合
    """

    dp = [False] * (n + 1)

    for i in range(n + 1):
        if i >= a and not dp[i - a]:
            dp[i] = True
        if i >= b and not dp[i - b]:
            dp[i] = True

    return dp[n]


def main():
    n, a, b = int_list()

    return "First" if dp_table(n, a, b) else "Second"


if __name__ == "__main__":
    print(main())
