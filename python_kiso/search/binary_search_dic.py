import math

def binary_search(numbers, goal_number):
    low = 0
    high = len(numbers)

#    while (low != high): # 検索したい値が存在しない場合は終了
    while (low <= high): # 検索したい値が存在しない場合は終了
        center = math.floor((low + high) / 2)
        if numbers[center] == goal_number:
            return(str(goal_number) + 'が' + str(center) + '番目にありました。')
        
        if(numbers[center] < goal_number):
            low = center + 1
            print("1) Low %d High %d" % (low,high))
        elif (goal_number < numbers[center]):
            high = center - 1
            print("1) Low %d High %d" % (low,high))
        else:
            break

numbers = [1,3,5,11,12,13,17,22,25,28]
print(numbers)
print('探したい数字を入力してください')
i = int(input())
print(binary_search(numbers, i))