def bubble_sort(numbers):
    
    for i in range(len(numbers)):
        for j in range(len(numbers)-1, i, -1):

            print(numbers)
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
    return numbers

numbers = [100,50,25,4,1]

print(bubble_sort(numbers))
bSort(numbers)
