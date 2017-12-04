def qsort(numbers):

    index_a = 0; index_b = len(numbers) - 1
    threshold = ( numbers[0] + numbers[-1] ) // 2
    
    print("threshold %d" % threshold)
    
    while index_a < index_b:
        for i in range(index_a,len(numbers)):
            if numbers[i] >= threshold:
                index_a = i + 1
                break
        
        for j in range(index_b,0,-1):
            if numbers[j] < threshold:
                index_b = j - 1
                break

        print("%d %d" % (i,j))
        
        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i] 
            print(numbers)
#        else:
#            break

    return numbers, i

def quick_sort(numbers):

    numbers, index = qsort(numbers) 
    print("================")
    print(numbers)
    print(index)
    print("================")
    return numbers

numbers = [4,8,6,5,2,1,3,9,7]

print(quick_sort(numbers))