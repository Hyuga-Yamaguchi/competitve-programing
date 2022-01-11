import math

n = int(input())

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


if __name__ == '__main__':
    data = get_sieve_of_eratosthenes(100)
    print(' '.join(map(str, data)))
    print("2～{0}までで以上が素数です\n".format(100))
