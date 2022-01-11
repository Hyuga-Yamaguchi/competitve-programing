n = int(input())

def dfs(s):
    if int(s) > n:
        return 0

    #三項演算子
    #条件式が真の時に返される値 if 条件式 else 条件式が偽の時に返される値
    ret = 1 if all(s.count(c) for c in "753") else 0 #s自体が七五三数なら　+1
    for c in "753":
        ret += dfs(s + c)
    return ret

print(dfs("0"))
