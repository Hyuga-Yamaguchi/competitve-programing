n = int(input())
xy = list(list(map(int, input().split())) for _ in range(n))

#print(n, xy)
x_minus_y = []
x_plus_y = []
for i in range(n):
    x_minus_y.append(xy[i][0] - xy[i][1])
    x_plus_y.append(xy[i][0] + xy[i][1])
x_max = max(x_minus_y)
x_min = min(x_minus_y)
y_max = max(x_plus_y)
y_min = min(x_plus_y)

if x_max - x_min >= y_max - y_min:
    print(x_max - x_min)
else:
    print(y_max - y_min)
