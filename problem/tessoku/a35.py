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


def calc_score(n, scores):
    dp = [[0] * n for _ in range(n)]
    dp[n - 1] = scores

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            if i % 2 == 0:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]


def main():
    n = int_input()
    scores = int_list()

    return calc_score(n, scores)


if __name__ == "__main__":
    print(main())
