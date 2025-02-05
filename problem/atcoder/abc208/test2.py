n=int(input())
txy=[list(map(int,input().split())) for i in range(n)]
def main():
    for i in range(n-1):
        dist=abs(txy[i][1]-txy[i+1][1])+abs(txy[i][2]-txy[i+1][2])
        print(i)
        if abs(txy[i][0]-txy[i+1][0])<dist:
            return False
            break
        else:
            if dist%2==abs(txy[i][0]-txy[i+1][0])%2:
                return True
            else:
                return False
                break
print("Yes" if main() else "No")
