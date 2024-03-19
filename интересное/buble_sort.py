def buble_sort(array):
    for _ in range(len(array) - 1):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array



# array = list(map(int, input('Введите числа через пробел для сортировки:').split()))
# n = len(array)
# print('Начальный массив:', array)
# count = 0
# for run in range(n - 1):
#     for i in range(n - 1):
#         if array[i] > array[i + 1]:
#             count += 1
#             array[i], array[i + 1] = array[i + 1], array[i]
# if count == 0:
#     print('Перестановок не требуется.')
# else:
#     print('Количество перестановок:', count)
#     print('Итоговый массив:', array)