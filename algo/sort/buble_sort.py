def buble_sort(array):
    for _ in range(len(array) - 1):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array

# print(buble_sort([1, 0, 2, 9, 3, 8, 4, 7, 5, 6, 10, -5]))