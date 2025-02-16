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


def coordinate_compression(arr):
    uniqure_sorted = sorted(set(arr))

    value_to_compressed = {value: idx for idx, value in enumerate(uniqure_sorted)}

    return [value_to_compressed[num] for num in arr]


def main():
    n = int_list()
    nums = int_list()

    return string_join(" ", [x + 1 for x in coordinate_compression(nums)])


if __name__ == "__main__":
    print(main())
