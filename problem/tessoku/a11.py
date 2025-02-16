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


import bisect


def bisect_index(arr, x):
    "Locate the leftmost value exactly equal to x"
    idx = bisect.bisect_left(arr, x)
    if idx != len(arr) and arr[idx] == x:
        return idx


def bisect_find_lt(arr, x):
    "Find rightmost value less than x"
    idx = bisect.bisect_left(arr, x)
    if idx:
        return arr[idx - 1]


def bisect_find_le(arr, x):
    "Find rightmost value less than or equal to x"
    idx = bisect.bisect_right(arr, x)
    if idx:
        return arr[idx - 1]


def bisect_find_gt(arr, x):
    "Find leftmost value greater than x"
    idx = bisect.bisect_right(arr, x)
    if idx != len(arr):
        return arr[idx]


def bisect_find_ge(arr, x):
    "Find leftmost item greater than or equal to x"
    idx = bisect.bisect_left(arr, x)
    if idx != len(arr):
        return arr[idx]


def main():
    n, x = int_list()
    a = int_list()

    return bisect_index(a, x) + 1


if __name__ == "__main__":
    print(main())
