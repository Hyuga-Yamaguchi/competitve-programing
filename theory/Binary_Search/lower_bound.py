#ソート済みの配列内でx以上のの値を持つもののうち、左側にある物は何か

#1.L=0,R=最後尾のインデックスとして以下の処理を繰り返す
#   1.L<=Rなら以下を実行する
#   2.LとRの中間にあるMが指す要素について、xとの代償関係を調べる
#       1.x未満ならば、右側半分にある部分配列に対して１と２の探索を行う(LとMがあった場所に移す)
#       2.x以上ならば、左側半分にある部分配列に対して1と２の探索を行う(RをMがあった場所に移す)
#2.Rが指す値が答え

# x以上のイテレータを
def lower_bound(arr , x):
    l = 0
    r = len(arr)
    for j in range(30):
        mid = (l + r) // 2
        # print(l , r , mid)
        if x <= arr[mid]:
            r = mid
        else:
            l = mid
    return r


arr=[1,4,5,8,10,24,55,66,190,256]
print(lower_bound(arr,55))#6を出力 #7を出力
print(lower_bound(arr,56))#7を出力　＃７
print(lower_bound(arr,4))#１を出力　＃2
print(lower_bound(arr,1))#0を出力　#1
print(lower_bound(arr,190))#8を出力 #9
print(lower_bound(arr,256))#9を出力 #-1
print(lower_bound(arr,1000))#-1を出力 #-1
print(lower_bound(arr,-1000))#0を出力 #0

print("------------------------------------")

arr=[1,1,1,2,3,3,4,5,5,5,5,6,7]
print(lower_bound(arr,1))#0 #-1
print(lower_bound(arr,2))
print(lower_bound(arr,3))
print(lower_bound(arr,4))
print(lower_bound(arr,5))
print(lower_bound(arr,6))
print(lower_bound(arr,7))
