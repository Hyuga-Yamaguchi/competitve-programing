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


from itertools import accumulate


def cumulative_sum_1d(arr, n, seg=False):
    if seg:
        ans = [0] * (n + 1)
        for l, r in arr:
            ans[l] += 1
            if r + 1 < len(ans):
                ans[r + 1] -= 1
        return list(accumulate(ans))[:-1]
    return list(accumulate(arr, initial=0))


def cumulative_sum_2d(arr, h, w, seg=False):
    cum = [[0] * (w + 1) for _ in range(h + 1)]
    if seg:
        ans = [[0] * (w + 1) for _ in range(h + 1)]
    else:
        for i in range(h):
            for j in range(w):
                cum[i + 1][j + 1] = (
                    arr[i][j] + cum[i][j + 1] + cum[i + 1][j] - cum[i][j]
                )
        return cum


def range_sum_1d(cum, l, r):
    return cum[r + 1] - cum[l]


def range_sum_2d(cum, l, r):
    x1, y1 = l
    x2, y2 = r
    return cum[x2 + 1][y2 + 1] + cum[x1][y1] - cum[x2 + 1][y1] - cum[x1][y2 + 1]


INF = 1 << 60


def main():
    h, w = int_list()
    xs = int_row_list(h)
    q = int_input()
    queries = int_row_list(q, dec=True)

    xs_cumsum = cumulative_sum_2d(xs, h, w)

    return string_join(
        "\n",
        [range_sum_2d(xs_cumsum, (x1, y1), (x2, y2)) for x1, y1, x2, y2 in queries],
    )


if __name__ == "__main__":
    print(main())
