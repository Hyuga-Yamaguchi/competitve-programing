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


def calc_vec(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2

    return tuple([x2 - x1, y2 - y1])


def add_vec(p, v):
    (x1, y1) = p
    (x2, y2) = v

    return tuple([x1 + x2, y1 + y2])


def main():
    m = int_input()
    search_stars = tuple(map(tuple, int_row_list(m)))
    n = int_input()
    photo_stars = set(map(tuple, int_row_list(n)))

    translations = {calc_vec(search_stars[0], ps) for ps in photo_stars}

    for translation in translations:
        if all(add_vec(star, translation) in photo_stars for star in search_stars):
            return " ".join(map(str, translation))


if __name__ == "__main__":
    print(main())
