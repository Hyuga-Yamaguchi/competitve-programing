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


INF = 1 << 60

from itertools import accumulate


def normal_cumsum_1d(arr):
    return list(accumulate(arr, initial=0))


def main():
    n, q = int_list()
    a = int_list()
    query = int_row_list(q, dec=True)

    cumsum_a = normal_cumsum_1d(a)

    return "\n".join([str(cumsum_a[r + 1] - cumsum_a[l]) for l, r in query])


if __name__ == "__main__":
    print(main())
