"""年齢当てゲーム
Aさんの年齢が20才以上36歳未満であることがわかっている時,
Aさんに４回までYes/No質問をするとき,
Aさんの年齢を当てることは可能か?
"""
print("Start Game!")

#Aさんの数の候補を表す区画を[left, right)と表す

left = 20
right = 36

#Aさんの数を１つに絞れない時は繰り返す
while right - left > 1:
    mid = left + (right - left) // 2

    #mid以上か聞いて、回答をyes/noで受け取る
    print("Is your age less than " + str(mid) + "? (yes/no)")
    ans = input()

    #回答に応じてありうる数の範囲を絞る
    if ans == "yes":
        right = mid
    else:
        left = mid

#年齢を当てる
print("Your age is " + str(left) + "!")
