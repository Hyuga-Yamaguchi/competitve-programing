n, m = map(int, input().split())
x, y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
#print(n,m,x,y,a,b)

time = 0#時刻
airport = 0#今いる空港　空港A=偶数,空港B=奇数

#二部探索用
def binary_search(arr,x):
    l = 0
    r = len(arr) - 1#数列arrの最後尾のインデックス
    while l <= r:
        mid = (l + r) // 2#中央値検索
        if x == arr[mid]:#ちょうど中央値に存在したとき
            return mid
        elif x < arr[mid]:#xが左側の配列に存在するとき
            r = mid - 1
        else:#xが右側の配列に存在するとき
            l = mid + 1
            #print(mid,r,l)
    return r + 1

#もし空港Aにいる場合は、time以上で最も小さいaiに乗る
#もし空港Bにいる場合は、time以上で最も小さいbiに乗る
while airport <= n + m :
    if airport % 2 == 0:
        a_index = binary_search(a,time)#time以上の配列aのindexを取得
        time = a[a_index] + x
        airport += 1
        #print(a_index,time,airport)
        if time > b[-1]:
            break
    elif airport % 2 == 1:
        b_index = binary_search(b,time)#time以上の配列bのindexを取得
        time = b[b_index] + y
        airport += 1
        #print(b_index,time,airport)
        if time > a[-1]:
            break


print(airport // 2)
