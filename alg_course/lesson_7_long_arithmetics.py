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



'''
Разбиение на 3 части
легко
# решено

# яндекс
Дан массив целых чисел nums. Нужно разбить его на три непрерывные непустые части. Верните минимально возможную сумму первых элементов каждой из частей после такого разбиения. Гарантируется, что разбиение всегда возможно.

Пример 1:

Ввод: nums = [3,1,2,4,5]
Вывод: 6
Объяснение: [3],[1],[2,4,5] → 3 + 1 + 2 = 6
Пример 2:

Ввод: nums = [5,2,1,3]
Вывод: 8
Объяснение: [5],[2],[1, 3] → 5 + 2 + 1 = 8
Ограничения:

len(nums) ≥ 3
'''


# мое решение
def min_split_cost(nums: List[int]) -> int:
    min1 = nums[0]
    min2 = min(nums[1], nums[2])
    min3 = max(nums[1], nums[2])

    for num in nums[3:]:
        if num < min2:
            min3 = min2
            min2 = num
        else:
            min3 = min(min3, num)

    return min1 + min2 + min3


# эталонное решение - ну тут хрень какая то с float, я не понял зачем
def min_split_cost(nums: List[int]) -> int:
    min1, min2 = float('inf'), float('inf')
    for i in range(1, len(nums)):
        if nums[i] < min1:
            min1, min2 = nums[i], min1
        elif nums[i] < min2:
            min2 = nums[i]
    return nums[0] + min1 + min2


# мое решение
def is_power_of_two(n: int) -> bool:
    while n != 1:
        if n % 2:
            return False
        n = n // 2
    return True


# эталонное решение

def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1) == 0)


'''
Сумма hex чисел
легко
# решено

# островок

# яндекс
Даны две строки s1 и s2, представляющие собой неотрицательные шестнадцатеричные числа (в нижнем регистре). Необходимо вернуть их сумму также в виде строки — шестнадцатеричного числа (в нижнем регистре).

Пример 1:

Ввод: s1 = "a", s2 = "5"
Вывод: "f"
Объяснение: 10 + 5 = 15, что в шестнадцатеричной системе равно "f"
Пример 2:

Ввод: s1 = "1a", s2 = "2b"
Вывод: "45"
Объяснение: 26 + 43 = 69, что в шестнадцатеричной системе равно "45"
Ограничения:

len(s1) ≥ 1
len(s2) ≥ 1
s1 и s2 содержат только символы '0'-'9' и 'a'-'f'

'''

# мое решение
def sum_hex(s1: str, s2: str) -> str:
    mapping = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }
    summ_s1 = 0
    for idx, char in enumerate(s1[::-1]):
        num = char
        if char in mapping:
            num = mapping[char]
        summ_s1 += int(num) * (16**idx)
    summ_s2 = 0

    for idx, char in enumerate(s2[::-1]):
        num = char
        if char in mapping:
            num = mapping[char]
        summ_s2 += int(num) * (16**idx)

    return str(hex(summ_s1 + summ_s2))[2:]


#эталонное решение
from typing import *

def sum_hex(s1: str, s2: str) -> str:
    result = []
    p1 = len(s1) - 1
    p2 = len(s2) - 1
    carry = 0

    # Пока есть цифры в одном из чисел или есть остаток переноса
    while p1 >= 0 or p2 >= 0 or carry > 0:
        if p1 >= 0:
            # Добавляем значение цифры из первого числа
            digit1 = int(s1[p1], 16)
            carry += digit1
            p1 -= 1
        if p2 >= 0:
            # Добавляем значение цифры из второго числа
            digit2 = int(s2[p2], 16)
            carry += digit2
            p2 -= 1
        # Вычисляем сумму текущих цифр по модулю 16
        digit_sum = carry % 16
        result.append(hex(digit_sum)[2:])
        # Обновляем перенос
        carry = carry // 16

    # Возвращаем результат в правильном порядке
    return ''.join(reversed(result))
