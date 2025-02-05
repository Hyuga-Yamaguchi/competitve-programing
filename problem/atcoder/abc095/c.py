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


def main():
    [a, b, c, x, y] = int_list()

    min_xy = min(x, y)
    cost = min_xy * 2 * c if a + b >= 2 * c else min_xy * (a + b)

    if x > y:
        cost += min(a * (x - y), 2 * c * (x - y))
    else:
        cost += min(b * (y - x), 2 * c * (y - x))

    return cost


if __name__ == "__main__":
    print(main())
