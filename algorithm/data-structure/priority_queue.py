import heapq


class PriorityQueue:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.heap_type = heap_type

    def push(self, value):
        if self.heap_type == "max":
            heapq.heappush(self.heap, -value)
        else:
            heapq.heappush(self.heap, value)

    def pop(self):
        if not self.heap:
            return None
        if self.heap_type == "max":
            return -heapq.heappop(self.heap)
        return heapq.heappop(self.heap)

    def top(self):
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


min_pq = PriorityQueue("min")
max_pq = PriorityQueue("max")

# 要素を追加
min_pq.push(5)
min_pq.push(3)
min_pq.push(8)
min_pq.push(1)

max_pq.push(5)
max_pq.push(3)
max_pq.push(8)
max_pq.push(1)

print("min_pq: ", min_pq.show())
print("max_pq: ", max_pq.show())

# 最小ヒープの動作確認
print("Min Heap")
print("Top (最小値):", min_pq.top())  # 1
print("Pop:", min_pq.pop())  # 1
print("Pop:", min_pq.pop())  # 3

# 最大ヒープの動作確認
print("\nMax Heap")
print("Top (最大値):", max_pq.top())  # 8
print("Pop:", max_pq.pop())  # 8
print("Pop:", max_pq.pop())  # 5
