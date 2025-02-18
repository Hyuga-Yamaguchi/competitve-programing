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


def bit_dp(n, m, coupons):
    dp = [[INF] * (1 << n) for _ in range(m + 1)]
    dp[0][0] = 0

    bit_coupons = [sum(x << i for i, x in enumerate(c)) for c in coupons]

    for i in range(1, m + 1):
        for j in range(1 << n):
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
            dp[i][j | bit_coupons[i - 1]] = min(
                dp[i][j | bit_coupons[i - 1]], dp[i - 1][j] + 1
            )

    result = dp[m][(1 << n) - 1]

    return result if result != INF else -1


def main():
    n, m = int_list()
    coupons = int_row_list(m)

    return bit_dp(n, m, coupons)


if __name__ == "__main__":
    print(main())
