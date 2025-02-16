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


def main():
    n, k = int_list()

    A = int_list()
    B = int_list()
    C = int_list()
    D = int_list()

    A_B = set(a + b for a in A for b in B)
    C_D = set(c + d for c in C for d in D)

    return "Yes" if any([k - c_d in A_B for c_d in C_D]) else "No"


if __name__ == "__main__":
    print(main())
