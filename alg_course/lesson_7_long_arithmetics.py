def summmm(nums1, nums2):
    p1 = len(nums1)-1
    p2 = len(nums2)-1
    curr_sum = []
    next_value = 0
    while p1 >=0 or p2 >=0:
        num1 = 0
        num2 = 0
        if p1>=0:
            num1 = nums1[p1]
        if p2>=0:
            num2 = nums2[p2]
        sub_sum = num1 + num2 + next_value
        if sub_sum < 10:
            curr_sum.append(sub_sum)
            next_value=0
        else:
            curr_sum.append(sub_sum%10)
            next_value=sub_sum//10

    i = 0
    j = len(curr_sum)-1
    while i <j:
        curr_sum[i], curr_sum[j] = curr_sum[j], curr_sum[i]
    return curr_sum

from typing import *

def min_possible_product(nums: List[int]) -> int:
    max1 = max(nums[0], nums[1])
    max2 = min(nums[0], nums[1])
    min1 = min(nums[0], nums[1])
    min2 = max(nums[1], nums[1])
    for num in nums[2:]:
        if num < min1:
            min2 = min1
            min1 = num
        else:
            min2 = min(min2, num)
        if num > max1:
            max2 = max1
            max1 = num
        else:
            max2 = max(max2, num)

    print(max1)
    print(max2)
    print(min1)
    print(min2)
    if min1 <= 0 and max1>0:
        return min1*max1
    elif min1 < 0 and max1 <=0:
        return max1*max2
    else:
        return min1*min2


min_possible_product([-1, -10, 0, -78, -2])


'''
Умножение длинного числа
средне
# решено

# яндекс
Дан массив чисел nums, представляющий собой число, записанное в обратном порядке. Также дано число n (1 ≤ n ≤ 9). Необходимо умножить nums на число n в столбик и вернуть в качестве результата изменённый массив nums.

Пример 1:

Ввод: nums = [3,2,1], n = 2
Вывод: [6,4,2]
Объяснение: 123 * 2 = 246 → [6,4,2]
Пример 2:

Ввод: nums = [0,0,9], n = 3
Вывод: [0,0,7,2]
Объяснение: 900 * 3 = 2700 → [0,0,7,2]
Ограничения:

len(nums) ≥ 1
0 ≤ nums[i] ≤ 9
nums не содержит ведущих нулей, кроме случая числа 0 ([0])
1 ≤ n ≤ 9
'''


# мое решение
def multiply(nums: List[int], n: int) -> List[int]:
    sub_sum = 0
    p = 0

    while p < len(nums):
        count = (nums[p] * n) + sub_sum
        summ = count % 10
        sub_sum = count // 10
        nums[p] = summ
        p += 1

    if sub_sum:
        nums.append(sub_sum)

    return nums


# эталонное решение
def multiply(nums: List[int], n: int) -> List[int]:
    carry = 0
    i = 0
    while i < len(nums) or carry:
        # Получаем текущую цифру или 0, если индекс вне массива
        current_digit = nums[i] if i < len(nums) else 0
        carry += current_digit * n

        if i < len(nums):
            # Обновляем текущую цифру
            nums[i] = carry % 10
        else:
            # Добавляем новую цифру
            nums.append(carry % 10)

        # Обновляем перенос
        carry //= 10
        i += 1
    return nums