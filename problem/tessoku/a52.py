import math
from collections import Counter, deque
import itertools

INF = 1 << 60
MOD1 = 10**9 + 7


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


def query_input(n, case_arg_types):
    """
    n: Number of queries
    case_arg_types: Args types list for case number
    """
    queries = []
    for _ in range(n):
        parts = input().split()
        case_num = parts[0]

        arg_types = case_arg_types.get(case_num, [])
        args = [arg_type(value) for arg_type, value in zip(arg_types, parts[1:])]

        queries.append((case_num, args))

    return queries


from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, value):  # O(1)
        self.queue.append(value)

    def pop(self):  # O(1)
        if not self.queue:
            return None
        return self.queue.popleft()

    def front(self):  # O(1)
        if not self.queue:
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def empty(self):
        return len(self.queue) == 0

    def show(self):
        return list(self.queue)


def string_join(sep, arr):
    return sep.join(map(str, arr))


def main():
    q = int_input()
    queries = query_input(q, {"1": [str], "2": []})

    qu = Queue()
    ans = []
    for case, args in queries:

        if case == "1":
            val = args[0]
            qu.push(val)
        elif case == "2":
            ans.append(qu.front())
        else:
            qu.pop()

    return string_join("\n", ans)


if __name__ == "__main__":
    print(main())
