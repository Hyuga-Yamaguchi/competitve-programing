def int_input():
    return int(input())


def int_list():
    return list(map(int, input().split()))


def int_row(N):
    return [int_input() for _ in range(N)]


def int_row_list(N):
    return [int_list() for _ in range(N)]


def str_input():
    return input()


def str_list():
    return list(input().split())


def str_row(N):
    return [str_input() for _ in range(N)]


def str_row_list(N):
    return [str_list() for _ in range(N)]


INF = 1 << 60

from itertools import permutations


def main():
    n = int_input()
    goods = int_row_list(n)

    unique_points = {e for g in goods for e in g}

    min_route_len = INF
    for e1, e2 in permutations(unique_points, 2):
        total_route = sum(
            min(
                abs(e1 - g1) + abs(g1 - g2) + abs(g2 - e2),
                abs(e1 - g2) + abs(g2 - g1) + abs(g1 - e2),
            )
            for g1, g2 in goods
        )
        min_route_len = min(min_route_len, total_route)

    return min_route_len


if __name__ == "__main__":
    print(main())
