# Data Structure

## Stack

```python
S = deque() # 空のdequeを返す O(1)
S.appned(x) # Sの一番上に要素を追加 O(1)
S[-1] # Sの一番上の要素を取得 O(1)
S.pop() # Sの一番上の要素を削除 O(1)
len(S) # Sの要素数を取得 O(1)
```

## Queue

```python
Q = deque() # 空のdequeを返す O(1)
Q.appned(x) # Sの最後尾に要素を追加 O(1)
Q[0] # Sの先頭要素を取得 O(1)
Q.popleft() # Sの先頭要素を削除 O(1)
len(Q) # Sの要素数を取得 O(1)
```
