def insertion_sort(numbers):
    '''
    Insertion Sort function, that sorts the array in ascending order
    Time Complexity: O(n^2)
    '''
    n = len(numbers)
    for i in range(1, n):
        insert_index = i
        curren_value = numbers.pop(i)
        for j in range(i-1, -1, -1):
            if numbers[j] > curren_value:
                insert_index = j
        numbers.insert(insert_index, curren_value)
    return numbers

numbers = [1, 4, 2, 3, 8, 9, 5, 7, 6, 10]
result = insertion_sort(numbers)
print(result)