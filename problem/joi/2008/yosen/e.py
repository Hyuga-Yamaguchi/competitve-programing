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


def reverse_cracker(arr):
    return list(map(lambda x: not x, arr))


INF = 1 << 60


def main():
    r, c = int_list()
    crackers = int_row_list(r)

    ans = 0
    for rev in bit_search(range(r), to_set=True):
        rec_cr = [
            reverse_cracker(cracker) if idx in rev else cracker
            for idx, cracker in enumerate(crackers)
        ]
        max_rev = 0
        for j in range(c):
            front = 0
            for i in range(r):
                if rec_cr[i][j]:
                    front += 1
            max_rev += max(front, r - front)
        ans = max(ans, max_rev)

    return ans


if __name__ == "__main__":
    print(main())
