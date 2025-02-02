n=int(input())
txy = [list(map(int,input().split())) for i in range(n)]
txy = [[0, 0, 0]] + txy
def main():
    flag = True
    for i in range(n):
        dist = abs(txy[i][1] - txy[i + 1][1]) + abs(txy[i][2] - txy[i + 1][2])
        if abs(txy[i][0] - txy[i + 1][0]) < dist:
            flag = False
        else:
            if dist % 2 != abs(txy[i][0] - txy[i + 1][0]) % 2:
                flag = False
    return flag
print("Yes" if main() else "No")
