def bubble_sort(arr):
    '''
    This function sort the array in ascending order using Bubble Sort Algorithm.
    Time Complexity: O(n2)
    '''
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            else:
                swapped = True
        if not swapped:
            return arr
    return arr


arr = [1, 4, 2, 3, 8, 9, 5, 7, 6, 10]
result = bubble_sort(arr)
print(result)