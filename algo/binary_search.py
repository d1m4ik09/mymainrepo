def binary_search(list, target):
    left = 0
    right = len(list) - 1
    mid = len(list) // 2
    
    while list[mid] != target and left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        else:
            if list[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

print(binary_search([5, 6, 7, 14, 16, 19, 25, 28, 30, 32, 34, 38, 42, 47, 50], 32))