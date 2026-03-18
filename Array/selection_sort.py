def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        min_value = numbers.pop(min_index)
        numbers.insert(i, min_value)
        #numbers[i], numbers[min_index]  = numbers[min_index], numbers[i]
    return numbers
        

numbers = [1, 4, 2, 3, 8, 9, 5, 7, 6, 10]
result = selection_sort(numbers)
print(result)