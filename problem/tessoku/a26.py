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


def grid_input(h):
    return [list(input().strip()) for _ in range(h)]


def string_join(sep, arr):
    return sep.join(map(str, arr))


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def eratosthenes(n, to_set=False):
    isprime = [True] * (n + 1)

    isprime[0] = False
    isprime[1] = False

    for p in range(2, n + 1):
        if not isprime[p]:
            continue
        q = p * 2
        while q <= n:
            isprime[q] = False
            q += p

    l = [i for i, _ in enumerate(isprime) if isprime[i]]

    return set(l) if to_set else l


def main():
    q = int_input()
    queries = int_row(q)
    max_q = 300000

    primes = eratosthenes(max_q, to_set=True)

    return string_join(
        "\n",
        ["Yes" if query in primes else "No" for query in queries],
    )


if __name__ == "__main__":
    print(main())
