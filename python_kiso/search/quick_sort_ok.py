def quicksort(seq):
    if len(seq) < 1:
        return seq

    pivot = seq[0]
    left = []
    right = []

    for x in range(1, len(seq)):
        if seq[x] <= pivot:
            left.append(seq[x])
        else:
            right.append(seq[x])

    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]

    return left + foo + right

numbers = [4,8,6,5,2,1,3,9,7]

print(quicksort(numbers))