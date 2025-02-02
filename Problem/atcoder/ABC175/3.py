import math

x,k,d = map(int,input().split())

ans = 0
if x == 0:
    if k % 2 == 0:
        ans = 0
    elif k % 2 == 1:
        ans = abs(d)
else :
    if abs(x) - k * d >= 0:
        ans = abs(abs(x) - k * d)
        #if abs(x) - k*d == 0:
            #if k - (abs(x) / (k * d)) % 2 == 0:
                #ans = 0
            #else:
                #ans = abs(x)
    elif abs(x) - k * d < 0:
        if  abs(x) - d * (abs(x) // d) != 0:
            if (k - (math.ceil(abs(x) / d))) % 2 == 1:
                ans = abs(abs(x) - d * (abs(x) // d))
            else:
                ans = abs(abs(x) - d * (abs(x) // d + 1))
        else:
            if (k - (math.ceil(abs(x) // d))) % 2 == 1:
                ans = d
            else:
                ans = 0
print(ans)
