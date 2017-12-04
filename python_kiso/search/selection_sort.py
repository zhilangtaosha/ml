def selection_sort(numbers):
    index = 0; value = 0
    for i in range(len(numbers)-1):

        value = numbers[i]

        for j in range(i+1, len(numbers)):

            if value > numbers[j]:

                value = numbers[j]
                index = j

        numbers[i], numbers[index] = numbers[index], numbers[i] 

    return numbers

numbers = [12,13,11,14,10]
print(selection_sort(numbers))
