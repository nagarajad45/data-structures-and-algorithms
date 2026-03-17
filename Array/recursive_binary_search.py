def recursive_binary_search(nums, target):
    '''
    This is a "recursive binary search" function to check whether the target value is in the list or not.
    Unlike non-recursive binary function, it returns True, If the target value is present. Otherwise, returns False.
    Not the index position of the target value.
    '''

    if len(nums) == 0:
        return False
    else:
        midpoint = (len(nums)) // 2

        if nums[midpoint] == target:
            return True
        else:
            if nums[midpoint] < target:
                return recursive_binary_search(nums[midpoint + 1:], target)
            else:
                return recursive_binary_search(nums[:midpoint], target)
            
def verify(result):
    print("Target found: ", result)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# checking for when target value is present
result = recursive_binary_search(nums, 3)
verify(result)

# checking for when target value is not present
result = recursive_binary_search(nums, 20)
verify(result)