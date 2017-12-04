#以下に線形探索法を行う関数を定義してください
def linear_search(numbears, goal):
    for i in  numbears:
        if i == goal:
            return i
    else:
        return 'None'

#def linear_search(numbers, goal_number):
#    index = 0; count = 0; flg_number_exists = 0
#    for number in numbers:
#        count += 1
#        if number == goal_number:
#            flg_number_exists = 1
#            break

#    if flg_number_exists == 1:
#        index = count - 1
#    else:
#        index = None
#    return index
    
numbers = [1,3,5,11,12,13,17,22,25,28]
print(numbers)
print('探したい数字を入力してください')
goal_number = int(input())

print(linear_search(numbers, goal_number))