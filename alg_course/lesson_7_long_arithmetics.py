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

'''
Разворот слов
легко
# решено

# островок

# яндекс
Дана строка s, содержащая символы латинского алфавита и пробелы. Нужно перевернуть только слова, оставив пробелы на своих местах.

Под словом подразумевается последовательность не пробельных символов. Пробельные блоки (одиночные или подряд идущие пробелы) должны остаться на своих местах, в тех же позициях, где они были изначально.

Пример 1:

Ввод: s = "hello world"
Вывод: "world hello"
Пример 2:

Ввод: s = "  this  is a test "
Вывод: "  test  a is this "
Пример 3:

Ввод: s = "one"
Вывод: "one"
Ограничения:

len(s) ≥ 1
s содержит пробелы и символы латинского алфавита
'''

# мое решение
def reverse_words(s: str) -> str:
    s_list = []
    submassive = []
    for char in s:
        if char != " ":
            submassive.append(char)
            continue
        if submassive:
            s_list.append("".join(submassive))
            submassive = []
        s_list.append(" ")
    if submassive:
        s_list.append("".join(submassive))
    p1 = 0
    p2 = len(s_list) - 1
    while p1 < p2 and p1 < len(s_list) and p2 >= 0:
        if s_list[p1] != " " and s_list[p2] != " ":
            s_list[p1], s_list[p2] = s_list[p2], s_list[p1]
            p1 += 1
            p2 -= 1
            continue
        elif s_list[p1] == " ":
            p1 += 1
        elif s_list[p2] == " ":
            p2 -= 1
    return "".join(s_list)


# эталонное решение
# Переворачивает порядок слов в строке, сохраняя позиции пробелов
def reverse_words(s: str) -> str:
    parts = []
    current = ''

    # В цонце цикла parts будет содержать подряд идущие пробельные и не пробельные символы
    for ch in s:
        # Если тип текущего блока изменился
        if current and (ch == ' ') != (current[0] == ' '):
            parts.append(current)
            current = ''
        current += ch

    # Добавляем последний блок, если он остался
    if current:
        parts.append(current)

    # Сохраняем только слова (не пробелы), чтобы потом их вставить в обратном порядке
    words = [p for p in parts if p[0] != ' ']

    # Собираем финальный результат: пробелы оставляем, слова берём с конца
    return ''.join(p if p[0] == ' ' else words.pop() for p in parts)


'''
Поиск монотонной последовательности
легко
# решено

# островок

# яндекс
Дан неотсортированный массив чисел nums. Необходимо найти монотонную последовательность максимальной длины (строго убывающую или строго возрастающую) и вернуть пару индексов начала и конца последовательности.

Пример 1:

Ввод: nums = [2,7,5,4,4,3]  
Вывод: [1,3]
Объяснение: монотонно убывающая последовательность [7,5,4] максимальной длины
Пример 2:

Ввод: nums = [15,1,3,5,10,7,4,3,1]
Вывод: [4,8]
Объяснение: монотонно убывающая последовательность [10,7,4,3,1] максимальной длины
Ограничения:

len(nums) >= 1
'''


# мое решение
def search_monoton(nums: List[int]) -> List[int]:
    max_seq = 1
    seq_list = [0, 0]
    p = 1
    asc = True
    current_seq = 1
    while p < len(nums):
        if nums[p] > nums[p - 1]:
            if asc is True:
                current_seq += 1
            else:
                asc = True
                current_seq = 2
        elif nums[p] < nums[p - 1]:
            if asc is False:
                current_seq += 1
            else:
                asc = False
                current_seq = 2
        else:
            current_seq = 1
        if current_seq > max_seq:
            seq_list = [p - current_seq + 1, p]
            max_seq = current_seq
        p += 1

    return seq_list


# эталонное решение
def search_monoton(nums: List[int]) -> List[int]:
    max_len = inc_len = dec_len = 1
    result = [0, 0]

    for idx in range(1, len(nums)):
        # последовательность возрастает
        if nums[idx - 1] < nums[idx]:
            inc_len += 1
            dec_len = 1
        # последовательность убывает
        elif nums[idx - 1] > nums[idx]:
            dec_len += 1
            inc_len = 1
        # сбрасываем последовательность
        else:
            inc_len = 1
            dec_len = 1

        # обновляем максимальную длину если
        # текущая длина больше предыдущей максимальной
        curr_len = max(inc_len, dec_len)
        if curr_len > max_len:
            result = [idx - curr_len + 1, idx]
            max_len = curr_len

    return result


'''
К ближайших чисел
легко
# решено

# вк

# островок

# яндекс
Дан массив nums, отсортированный в неубывающем порядке, индекс idx и число k. Нужно найти k ближайших к значению nums[idx] чисел в массиве и вернуть в любом порядке. При равных расстояниях предпочтение отдаётся меньшим числам.

Пример 1:

Ввод: nums = [2,5,5,5,8], idx = 2, k = 4
Вывод: [2,5,5,5]
Объяснение: ответ [2,5,5,5], а не [5,5,5,8], потому что 2 < 8 при abs(8-5) = abs(2-5)
Пример 2:

Ввод: nums = [-100,1,2,5,8,9], idx = 4, k = 2
Вывод: [8,9]
Ограничения:

len(nums) >= 1
0 <= idx < len(nums)
k >= 0
'''

# мое решение
def find_nearest_numbers(nums: List[int], idx: int, k: int) -> List[int]:
    result = []
    p1 = idx - 1
    p2 = idx + 1
    if k > 0:
        result.append(nums[idx])
    k-=1
    while k > 0:
        if p1 < 0 and p2 >= len(nums):
            return result
        if p1 < 0:
            result.append(nums[p2])
            p2+=1
            k-=1
            continue
        if p2 >= len(nums):
            result.append(nums[p1])
            p1-=1
            k-=1
            continue
        diff1 = abs(nums[idx] - nums[p1])
        diff2 = abs(nums[idx] - nums[p2])

        if diff1 <= diff2:
            result.append(nums[p1])
            p1-=1
            k-=1
        else:
            result.append(nums[p2])
            p2+=1
            k-=1
    return result


# эталонное решение
from typing import *

def find_nearest_numbers(nums: List[int], idx: int, k: int) -> List[int]:
    if k == 0:
        return []
    # добавляем в ответ nums[idx]
    result = [nums[idx]]
    # l - индекс кандидата на добавление слева от idx
    # r - индекс кандидата на добавление справа от idx
    l, r = idx - 1, idx + 1
    for _ in range(k - 1):
        if r >= len(nums) or l >= 0 and abs(nums[idx] - nums[l]) <= abs(nums[idx] - nums[r]):
            result.append(nums[l])
            l -= 1
        else:
            result.append(nums[r])
            r += 1
    return result



def compare(s: str, t: str) -> bool:
    p1 = len(s) - 1
    p2 = len(t) - 1
    skip1 = 0
    skip2 = 0
    while p1 >= 0 or p2 >= 0:
        print(f'{p1} {p2}')
        if p1>=0 and s[p1] == '#':
            skip1+=1
            p1-=1
            continue
        if p2>=0 and t[p2] == '#':
            skip2+=1
            p2-=1
            continue
        if skip1 > 0:
            p1-=1
            skip1-=1
            continue
        if skip2 > 0:
            p2-=1
            skip2-=1
            continue
        if p1 < 0 or p2 <0:
            return False
        if s[p1] != t[p2]:
            return False
        p1-=1
        p2-=1
    return True
#
#
# t = 'aaaa###a'
# s = 'aaa###a'
#
# compare(s, t)



def remove_duplicates(nums: List[int]) -> List[int]:
    hash_map = set()
    p1 = 0
    p2 = len(nums) - 1
    while p1 < len(nums) and p1 <= p2:
        print(f'{p1} {p2}')
        if nums[p1] in hash_map:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p2-=1
            continue
        else:
            hash_map.add(nums[p1])
            p1+=1

    return nums[:p2+1]


# remove_duplicates([1, 2, 2])


def max_area(height: List[int]) -> int:
    _max_area = 0
    p1 = 0
    p2 = len(height) - 1
    while p1 < p2:
        curr_area = min(height[p1], height[p2]) * (p2 - p1)
        _max_area = max(_max_area, curr_area)
        if p1 > p2:
            p2 -= 1
        else:
            p1 += 1

    return _max_area

#
# nums = [2, 3, 4, 5, 18, 17, 6]
#
# max_area(nums)


def find_duplicate_num(nums: List[int]) -> int:
    '''
    [3, 1, 3, 4, 2]
    [0 ,1 ,2, 3, 4]
    Алгоритм Флойда - поиск цикла в связном списке
    Вот мы нашли, что есть цикл. Теперь надо найти голову
    '''
    slow = nums[0]
    fast = nums[0]
    while fast < len(nums) and slow < len(nums):
        if nums[fast] == nums[slow]:
            break
        else:
            slow = nums[slow]
            fast = nums[nums[fast]]

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

nums = [3, 1, 3, 4, 2]

find_duplicate_num(nums)