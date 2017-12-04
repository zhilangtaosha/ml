import math

def binary_search(numbers, TARGET):
    low = 0
    high = len(numbers) #なぜ-1いれると動かない。。。

    while (low != high): # 検索したい値が存在しない場合は終了
        center = math.floor((low + high) / 2)
        if(goal_number == numbers[center]):
            return center
        elif (numbers[center] < TARGET):
            low = center + 1
            print("1) Low %d High %d" % (low,high))
#            for i in numbers[low:high]:print(i)
        elif (TARGET < numbers[center]):
            high = center - 1
            print("2) Low %d High %d" % (low,high))
        else:
            break

numbers = [1,3,5,11,12,13,17,22,25,28]
print(numbers)
print('探したい数字を入力してください')
goal_number= int(input())
print(binary_search(numbers, goal_number))
