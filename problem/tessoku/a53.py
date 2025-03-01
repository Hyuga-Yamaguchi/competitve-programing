import math
from collections import Counter, deque
import itertools
from heapq import heappush, heappop

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


def string_join(sep, arr):
    return sep.join(map(str, arr))


import heapq


class PriorityQueue:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.heap_type = heap_type

    def push(self, value):  # O(logN)
        if self.heap_type == "max":
            heapq.heappush(self.heap, -value)
        else:
            heapq.heappush(self.heap, value)

    def pop(self):  # O(logN)
        if not self.heap:
            return None
        if self.heap_type == "max":
            return -heapq.heappop(self.heap)
        return heapq.heappop(self.heap)

    def top(self):  # O(1)
        if not self.heap:
            return None
        if self.heap_type == "max":
            return -self.heap[0]
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def show(self):
        return self.heap


def main():
    q = int_input()
    queries = query_input(q, {"1": [int], "2": []})

    hq = PriorityQueue("min")
    ans = []

    for case, args in queries:

        if case == "1":
            val = args[0]
            hq.push(val)
        elif case == "2":
            ans.append(hq.top())
        else:
            hq.pop()

    return string_join("\n", ans)


if __name__ == "__main__":
    print(main())
