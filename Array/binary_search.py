def binary_search(nums, tagret):
    '''
    This function returns index value of target, if it is found in list.
    Otherwise, it returns None.

    Input: Sorted Array (ascending order) and target value
    Output: Index number (if found) or None ( if not found)

    Time Complexity: O(log n)
    '''

    first = 0
    last = len(nums) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if nums[midpoint] == tagret:
            return midpoint
        elif nums[midpoint] < tagret:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(result):
    if result is not None:
        print(f"Target found at index: {result}")
    else:
        print("Target not found")
    

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# checking for when target value is present
result = binary_search(nums, 3)
verify(result)

# checking for when target value is not present
result = binary_search(nums, 12)
verify(result)

