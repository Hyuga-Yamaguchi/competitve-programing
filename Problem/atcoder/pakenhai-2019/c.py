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
    [n, m] = int_list()
    a = int_row_list(n)

    max_score = 0
    for song1 in range(m):
        for song2 in range(m):
            sum_score = 0
            for student in range(n):
                sum_score += max(a[student][song1], a[student][song2])
            if sum_score > max_score:
                max_score = sum_score

    return max_score


if __name__ == "__main__":
    print(main())
