import heapq

a = [12, 15, 3, 7, 5, 3, 19, 1, 2, 10 ,6, 7]
heapq.heapify(a) #リストを優先度付きキューへ
print(a)

#最小値の取り出し #計算量:O(1)
print(heapq.heappop(a))
print(a)

#要素の挿入
heapq.heappush(a, -2)
print(a)
