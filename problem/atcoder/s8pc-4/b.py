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


def bit_search(arr, to_set=False):
    n = len(arr)
    return [
        (
            {arr[j] for j in range(n) if i >> j & 1}
            if to_set
            else [arr[j] for j in range(n) if i >> j & 1]
        )
        for i in range(1 << n)
    ]


from functools import reduce


def calc_add_height(arr):
    after_bldgs = reduce(lambda acc, x: acc + [max(acc[-1] + 1, x)], arr[1:], [arr[0]])
    height = sum(max(0, x - y) for x, y in zip(after_bldgs, arr))

    return height


INF = 1 << 60


def main():
    n, k = int_list()
    buildings = int_list()

    ans = INF
    for bldgs in bit_search(buildings[1:]):
        target_bldgs = [buildings[0]] + bldgs
        if len(target_bldgs) >= k:
            ans = min(ans, calc_add_height(target_bldgs))

    return ans


if __name__ == "__main__":
    print(main())
