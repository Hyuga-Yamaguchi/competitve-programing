#二分探索(x以下の最大値)
def upper_bound(arr,x):
    l=0
    r=len(arr)-1#数列arrの最後尾のインデックス
    while l<=r:
        mid=(l+r)//2#中央値検索
        if x==arr[mid]:#ちょうど中央値に存在したとき
            return mid-1
        elif x<arr[mid]:#xが左側の配列に存在するとき
            r=mid-1
        else:#xが右側の配列に存在するとき
            l=mid+1
        #print(mid,r,l)
    if x<=arr[0]:
        return -1
    else:
        return r

arr=[1,4,5,8,10,24,55,66,190,256]
print(upper_bound(arr,55))#6を出力 #5
print(upper_bound(arr,56))#6を出力 #6
print(upper_bound(arr,4))#１を出力 #0
print(upper_bound(arr,3))#0を出力 #0
print(upper_bound(arr,190))#8を出力 #7
print(upper_bound(arr,256))#9を出力 #8
print(upper_bound(arr,1000))#9を出力 #9
print(upper_bound(arr,1))#0を出力　#-1
print(upper_bound(arr,-1000))#-1を出力
