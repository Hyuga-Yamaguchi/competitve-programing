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


def cumulative_sum(arr, seg=False, seg_n=0):
    if seg:
        ans = [0] * (seg_n + 1)
        for l, r in arr:
            ans[l] += 1
            if r + 1 < len(ans):
                ans[r + 1] -= 1
        return list(accumulate(ans))[:-1]
    else:
        return list(accumulate(arr, initial=0))


INF = 1 << 60


def main():
    d = int_input()
    n = int_input()
    query = int_row_list(n, dec=True)

    return string_join(
        "\n",
        cumulative_sum(
            query,
            seg=True,
            seg_n=d,
        ),
    )


if __name__ == "__main__":
    print(main())
