import math

t = int(input())

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

for i in range(t):
    n, s, k = map(int,input().split())
    d = math.gcd(math.gcd(n,s),k)
    #print(d)
    a = k // d; b = (n - s) // d; m = n // d
    #print(a, b, m)

    if math.gcd(a, m) != 1:
        print(-1)
    else:
        #print(modinv(a, m))
        print(b * modinv(a, m) % m)
