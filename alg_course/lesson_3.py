from typing import *
'''
Условие
Дан массив nums. Нужно переместить все нули (0) в конец массива, при этом порядок остальных элементов должен сохраниться.

Необходимо изменять исходный массив напрямую, без создания нового массива для хранения результата.

Пример
Ввод: nums = [2,1,0,0,4,0,9]
Вывод: [2,1,4,9,0,0,0]
'''
nums = [2,1,0,0,4,0,9]
# мое решение
def swap(test_list: List) -> List:
    p1 = len(test_list) - 1
    p2 = len(test_list) - 1
    while p1>=0:
        if test_list[p1] != 0:
            p1 -= 1
            continue
        else:
            i = p2 - p1
            for j in range(i):
                nums[p1+j], nums[p1+j+1] = nums[p1+j+1], nums[p1+j]
            p2 -=1
            p1 -=1
    return test_list

print(swap(nums))

'''
[2,1,0,0,4,3,9]
[0,1,2,3,4,5,6]
p1 = 3
p2 = 6
p2 - p1 = количество итераций
for i in range(3):

3 и 4
4 и 5
5 и 6
'''

# эталонное решение
def move_zeros(nums: List[int]) -> List[int]:
    # указывает на какую позицию поставим следующий элемент не равный 0
    p1 = 0
    # указывает на следующий не нулевой элемент
    p2 = 0
    while p2 < len(nums):
        if nums[p2] != 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
        p2 += 1
    return nums