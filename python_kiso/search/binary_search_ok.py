import math

def binary_search(list, item):
    low = 0                        # lowとhighを使ってリストの検索部分を追跡
    high = len(list) - 1
    while low <= high:             # 1つの要素に絞り込まれるまでの間は...
        mid = (low + high) // 2
        guess = list[mid]          # 真ん中の要素を調べる
        if guess == item:          # アイテムを検出
            return mid
        if guess > item:           # 推測した数字が大きすぎた
            high = mid - 1
        else:                      # 推測した数字が小さすぎた
            low = mid + 1
    return None   

numbers = [1,3,5,11,12,13,17,22,25,28]
print(numbers)
print('探したい数字を入力してください')
goal_number= int(input())
print(binary_search(numbers, goal_number))
