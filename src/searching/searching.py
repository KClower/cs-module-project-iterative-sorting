def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
            
    return -1
    # if len(arr) <= 1:
    #     pass

    # first = 0
    # last = (len(arr) - 1)

    # while first <= last:
    #     middle = (first + last) // 2

    #     if arr[middle] == target:
    #         return False
        
    #     else:
    #         if target < arr[middle]:
    #             last = middle - 1
    #         else:
    #             if target > arr[middle]:
    #                 first = middle + 1


    return -1  # not found
