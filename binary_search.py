def binary_search(data: list, item):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = data[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


print(binary_search(list(range(1, 101)), 3))
print(binary_search(list(range(1, 101)), 110))


# Tasks
'''
Для отсортированного списка из 128 имен понадобится log2 128 проверок для поиска значения методом бинарного поиска.
То есть 7 проверок. 
Если этот список увеличить вдвое, количество проверок увеличиться на 1 единицу.

'''