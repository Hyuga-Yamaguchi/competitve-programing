s_count=int(input())
s=list(map(int,input().split()))
t_count=int(input())
t=list(map(int,input().split()))

#print(s_count)
#print(s)
#print(t_count)
#print(t)

#二部探索
def binary_search(arr,x):
    l=0
    r=len(arr)-1#数列arrの最後尾のインデックス
    while l<=r:
        mid=(l+r)//2#中央値検索
        if x==arr[mid]:#ちょうど中央値に存在したとき
            return mid
        elif x<arr[mid]:#xが左側の配列に存在するとき
            r=mid-1
        else:#xが右側の配列に存在するとき
            l=mid+1
        #print(mid,r,l)
    if x==arr[r]:
        return r
        #print(r)
    return -1#存在しない時

count=0
for i in range(t_count):
    if binary_search(s,t[i])!=-1:
        count+=1
    else:
        count+=0
print(count)
