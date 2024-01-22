def quicksort_function(array):
    if len(array) < 2:
        return array
    
    pivot = array[len(array) // 2]
    left = [i for i in array if i < pivot]
    middle = [i for i in array if i == pivot]
    right = [i for i in array if i > pivot]

    return quicksort_function(left) + middle + quicksort_function(right)


# test cases
print(quicksort_function([10, 5, 2, 3])) # [2, 3, 5, 10]
print(quicksort_function([1, 2, 3, 4])) # [1, 2, 3, 4]
print(quicksort_function([1, 1, 1, 1])) # [1, 1, 1, 1]