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


def segment_dp(n, points):
    dp = [[0] * n for _ in range(n)]

    for l in range(n):
        for r in range(n - 1, l - 1, -1):
            left_score = points[l - 1][1] if l > 0 and l <= points[l - 1][0] <= r else 0
            right_score = (
                points[r + 1][1] if r < n - 1 and l <= points[r + 1][0] <= r else 0
            )

            dp[l][r] = max(
                dp[l][r + 1] + right_score if r < n - 1 else 0,
                dp[l - 1][r] + left_score if l > 0 else 0,
            )
    return max(dp[i][i] for i in range(n))


def main():
    n = int_input()
    points = [[idx - 1, point] for idx, point in int_row_list(n)]

    return segment_dp(n, points)


if __name__ == "__main__":
    print(main())
