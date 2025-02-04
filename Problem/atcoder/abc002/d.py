def int_input():
    return int(input())


def int_list():
    return list(map(int, input().split()))


def int_row(N):
    return [int_input() for _ in range(N)]


def int_row_list(N, dec=False):
    return [int_list() for _ in range(N)]


def str_input():
    return input()


def str_list():
    return list(input().split())


def str_row(N):
    return [str_input() for _ in range(N)]


def str_row_list(N):
    return [str_list() for _ in range(N)]


from itertools import combinations


def bit_search(arr):
    n = len(arr)
    return [[arr[j] for j in range(n) if i >> j & 1] for i in range(1 << n)]


INF = 1 << 60


def main():
    n, m = int_list()
    relations = {(x - 1, y - 1) for x, y in int_row_list(m)}

    ans = 0
    for ps in bit_search(range(n)):
        if all((x, y) in relations for x, y in combinations(ps, 2) if x < y):
            ans = max(ans, len(ps))
    return ans


if __name__ == "__main__":
    print(main())
