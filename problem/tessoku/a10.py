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


def cumulative_max(arr, n):
    cummax = [0] * (n + 1)
    for i in range(1, n + 1):
        cummax[i] = max(arr[i - 1], cummax[i - 1])
    return cummax


INF = 1 << 60


def main():
    n = int_input()
    rooms = int_list()
    d = int_input()
    queries = int_row_list(d, dec=True)

    cummax_rooms = cumulative_max(rooms, n)
    cummax_rooms_reverse = cumulative_max(rooms[::-1], n)

    return string_join(
        "\n",
        [max(cummax_rooms[l], cummax_rooms_reverse[n - r - 1]) for l, r in queries],
    )


if __name__ == "__main__":
    print(main())
