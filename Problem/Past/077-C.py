n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

#リストをソート
a=sorted(a)
b=sorted(b)
c=sorted(c)

"""二分探索(x以上の最小値index) !同じ値の時はindex+1をする"""
def lower_bound(arr,x):
    l = 0
    r = len(arr) - 1#数列arrの最後尾のインデックス
    while l <= r:
        mid = (l + r) // 2#中央値検索
        if x == arr[mid]:#ちょうど中央値に存在したとき
            return mid + 1
        elif x < arr[mid]:#xが左側の配列に存在するとき
            r = mid - 1
        else:#xが右側の配列に存在するとき
            l = mid + 1
        #print(mid,r,l)
    if x > arr[-1]:
        return -1
    else:
        return r + 1

"""二分探索(x以下の最大値) !同じ値の時はindex-1をする"""
def upper_bound(arr,x):
    l = 0
    r = len(arr) - 1#数列arrの最後尾のインデックス
    while l <= r:
        mid = (l + r) // 2#中央値検索
        if x == arr[mid]:#xがちょうど中央値に存在したとき
            return mid - 1
        elif x < arr[mid]:#xが左側の配列に存在するとき
            r = mid - 1
        else:#xが右側の配列に存在するとき
            l = mid + 1
        #print(mid,r,l)
    if x <= arr[0]:
        return -1
    else:
        return r

#個数をカウント
count=0
for i in range(n):
    a_count = upper_bound(a,b[i]) + 1#b要素固定でのa要素の個数
    c_count = lower_bound(c,b[i]) + 1#b要素固定でのc要素の個数
    if a_count == 0 or c_count == 0:
        count += 0
    else:
        count += a_count * (len(c) - c_count + 1)
        print(upper_bound(a,b[i]),lower_bound(c,b[i]))
        print(a_count,len(c),c_count,len(c) - c_count + 1)
        print(count)

print(count)
