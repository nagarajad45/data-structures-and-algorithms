def linear_search(nums, target):
    '''
    This function returns index value of target, if it is found in list.
    Otherwise, it returns None.
    '''
    for i in range(len(nums)):
        if nums[i] == target:
            return i  
    return None

def verify(result):
    if result is not None:
        print(f"Target value found at {result}")
    else:
        print("Target value is not found.")

nums = [1, 4, 2, 3, 8, 9, 5, 7, 6, 10]
result = linear_search(nums, 10)
verify(result)