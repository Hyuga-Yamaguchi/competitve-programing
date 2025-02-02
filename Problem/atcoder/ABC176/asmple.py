wx_wy = []
for i in range(-2 ,3):
    for j in range(-2, 3):
        if [i, j] == [1, 0] or [i, j] == [0, 1] or [i, j] == [-1, 0]or [i, j] == [0, -1]:
            pass
        else:
            wx_wy.append([i, j])
print(wx_wy)
