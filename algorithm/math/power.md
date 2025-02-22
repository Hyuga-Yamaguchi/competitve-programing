# Power

繰り返し二乗法

## 実装

```python
def power(a, b, m):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result
```

## 考え方

- $a^1 \times a^1 = a^2$
- $a^2 \times a^2 = a^4$
- $a^4 \times a^4 = a^8$
- $a^8 \times a^8 = a^{16}$
- ...

を計算する。これらから、 $a^{42} = a^2 \times a^8 \times a^{32}$ , $a^{39} = a^1 \times a^2 \times a^{4} \times a^{32}$ のように計算する。
