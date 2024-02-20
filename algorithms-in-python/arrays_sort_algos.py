# 1. Bubble Sort: O(n^2): https://www.youtube.com/watch?v=xli_FI7CuzA
def bubble_sort(my_list):
    # Traverse through all array elements
    for i in range(len(my_list)):
        # Last i elements are already in place
        for j in range(0, len(my_list) - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

# 2. Selection Sort: O(n^2): https://www.youtube.com/watch?v=g-PGLbMth_g
def selection_sort(my_list):
    # Traverse through all array elements
    for i in range(len(my_list)):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
        # Swap the found minimum element with the first element
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

# 3. Insertion Sort: O(n^2): https://www.youtube.com/watch?v=JU767SDMDvA
def insertion_sort(my_list):
    # Traverse through 1 to len(arr)
    for i in range(1, len(my_list)):
        key = my_list[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key

# 4. Merge Sort: O(n log n), Worst Case: O(n log n) https://www.youtube.com/watch?v=4VqmGXwpLqc
def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2 # Finding the middle of the list
        left_half = my_list[:mid] # Dividing the list elements into 2 halves
        right_half = my_list[mid:]

        merge_sort(left_half) # Sorting the first half
        merge_sort(right_half)

        i = j = k = 0 # Initializing the index variables
        # Copy data to temp lists left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1

    return my_list

# 5. Quick Sort: O(n log n), Worst Case: O(n^2) https://www.youtube.com/watch?v=Hoixgm4-P4M
def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        pivot = my_list.pop() # Choosing the last element as the pivot
        less = [x for x in my_list[0:] if x <= pivot]
        greater = [x for x in my_list[0:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
