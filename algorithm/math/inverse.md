# Inverse

逆元

## 概要

$p$ と $a$ が互いに素であるときに、 $\mod p$ における $a$ の逆元が存在し、フェルマーの小定理より、 $a^{-1} = a^{p - 2}$ である。

よって、 $m$ , $n$ を整数とする時、

$m \div n \equiv m \times n^{p - 2} \mod p$

である。

## フェルマーの小定理

$p$ が素数で、 $a$ が $p$ の倍数でない正の整数の時、 $a^{p - 1} \equiv 1 \mod p$

### 証明

まず、$a$ と $p$ が互いに素な時、 $a$ , $2a$ , $3a$ , ... , $(p - 1)a$ を $p$ で割った余りは全て異なることを示す。 (1)

$1 \leq i < j \leq p - 1$ を満たす整数 $i$ , $j$ について、$ia$ と $ja$ を $p$ で割った甘利が等しいとすると、 $(i - j)a$ は $p$ の倍数になるはずだが、 $1 \leq i - j < b$ かつ $a$ と $p$ は互いに素なため矛盾する。よって、(1)を示した。

これより、 $a$ , $2a$ , $3a$ , ... , $(p - 1)a$ を $p$ で割った余りは $1$ から $p - 1$ の順列であり、

$\prod\limits_{k=1}^{p-1}ka \equiv (p - 1)! \mod p$

である。$(p - 1)!$ と $p$ は互いに素なので両辺を $(p - 1)!$ で割って、

$a^{p - 1} \equiv 1 \mod p$

### 実装

Pythonでは、 組み込みの`pow`関数にその機能が実装されている。

例えば、 $38^{-1} \mod 97$ は、

```python
>>> pow(38, -1, 97)
23
>>> pow(38, 95, 97)
23
```

で計算可能である、ちなみに、

```python
>>> 23 * 38 % 97
1
```

を満たす。

また、$a$ と $p$ が互いに袖ない場合は、エラーを返す。

```python
>>> pow(18, -1, 12)
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    pow(18, -1, 12)
    ~~~^^^^^^^^^^^^
ValueError: base is not invertible for the given modulus
```
