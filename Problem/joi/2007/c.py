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


def rotate(direction, vector):
    (x, y) = vector
    return tuple(map(lambda co: co * direction, [-y, x]))


def vector_sum(v1, v2):
    return tuple(map(lambda x, y: x + y, v1, v2))


def calc_square(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def main():
    n = int(input().strip())
    coos = {tuple(map(int, input().split())) for _ in range(n)}

    max_square = 0
    for x1, y1 in coos:
        for x2, y2 in coos - {(x1, y1)}:
            vector = (x2 - x1, y2 - y1)
            rev_vector = (-vector[0], -vector[1])

            rotated1 = rotate(1, vector)
            rotated2 = rotate(-1, vector)

            if (
                vector_sum((x1, y1), rotated1) in coos
                and vector_sum((x2, y2), rotate(-1, rev_vector)) in coos
            ) or (
                vector_sum((x1, y1), rotated2) in coos
                and vector_sum((x2, y2), rotate(1, rev_vector)) in coos
            ):
                max_square = max(max_square, calc_square(x1, y1, x2, y2))

    return max_square


if __name__ == "__main__":
    print(main())
