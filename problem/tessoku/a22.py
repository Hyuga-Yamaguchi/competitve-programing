INF = 1 << 60


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


def string_join(sep, arr):
    return sep.join(map(str, arr))


def dp_table(n, a, b):
    dp = [-INF] * n
    dp[0] = 0

    for i in range(n - 1):
        if dp[i] < 0:  # 到達不可能点をスキップする
            continue
        dp[a[i]] = max(dp[a[i]], dp[i] + 100)
        dp[b[i]] = max(dp[b[i]], dp[i] + 150)

    return dp[-1]


def main():
    n = int_input()
    a = int_list(dec=True)
    b = int_list(dec=True)

    return dp_table(n, a, b)


if __name__ == "__main__":
    print(main())
