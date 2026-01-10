'''
Дан массив nums, отсортированный по возрастанию.
Нужно вернуть отсортированный массив, полученный путём взятия модуля от каждого элемента nums.

Проще говоря, все отрицательные элементы нужно заменить на их положительные значения,
и итоговый массив вернуть в отсортированном порядке.

Ввод: nums = [-3,-2,0,1,3,5]
Вывод: nums = [0,1,2,3,3,5]
'''

from typing import *
def sorted_nums(nums: List) -> List:
    result = []
    p1 = 0
    p2 = len(nums) - 1
    while p1 <= p2:
        if abs(nums[p1]) > abs(nums[p2]):
            result.append(abs(nums[p1]))
            p1 += 1
        else:
            result.append(abs(nums[p2]))
            p2 -=1
    return list(reversed(result))


from typing import *

def two_sum(nums: List[int], target: int) -> List[int]:
    p1 = 0
    p2 = len(nums) - 1
    print(len(nums))
    result = []
    while nums[p1] + nums[p2] != target:
        if nums[p2] > target:
            p2 -=1
        else:
            p1 +=1
        print(p1)
        print(p2)
        print(f'сумма = {nums[p1] + nums[p2]}')
    return [p1+1, p2+1]

target = 542; nums = [12, 13, 23, 28, 43, 44, 59, 60, 61, 68, 70, 86, 88, 92, 124, 125, 136, 168, 173, 173, 180, 199, 212, 221, 227, 230, 277, 282, 306, 314, 316, 321, 325, 328, 336, 337, 363, 365, 368, 370, 370, 371, 375, 384, 387, 394, 400, 404, 414, 422, 422, 427, 430, 435, 457, 493, 506, 527, 531, 538, 541, 546, 568, 583, 585, 587, 650, 652, 677, 691, 730, 737, 740, 751, 755, 764, 778, 783, 785, 789, 794, 803, 809, 815, 847, 858, 863, 863, 874, 887, 896, 916, 920, 926, 927, 930, 933, 957, 981, 997];

# two_sum(nums, target)

'''
Самый большой контейнер
средне
# решено

# яндекс
Дан массив целых чисел nums, nums[i] – высота линии. Нужно найти максимальную площадь, которую может заполнить вода между двумя линиями.

ВАЖНО: площадь воды считается как min(nums[i], nums[j]) * (j - i), где i – индекс первой линии, а j - номер второй.

'''

def max_area(height: List[int]) -> int:
    curr = 0
    p1 = 0
    p2 = len(height) - 1
    while p1 <= p2:
        print(p1)
        print(p2)
        new_curr = (p2-p1)*min(height[p1], height[p2])
        print(f'new_curr = {new_curr}')
        if new_curr > curr:
            curr = new_curr
        if height[p1] < height[p2]:
            p1+=1
        else:
            p2-=1
    return curr

nums = [2, 3, 4, 5, 18, 17, 6]

# max_area(nums)

'''
Дана строка s. Верните true, если s является палиндромом, или false в противном случае. Фраза является палиндромом, если после преобразования всех заглавных букв в строчные и удаления всех символов, кроме букв и цифр, она читается одинаково слева направо и справа налево.

Буквенно-цифровые символы включают латинские буквы и цифры.

Пример 1:

Ввод: s = "A man, a plan, a canal: Panama"
Вывод: true
Объяснение: строка "amanaplanacanalpanama" является палиндромом
Пример 2:

Ввод: s = "AbaCdaba"
Вывод: false
Ограничения:

len(s) >= 1
'''

def is_palindrome(s: str) -> bool:
    s = s.lower()
    p1 = 0
    p2 = len(s) - 1
    while p1 <= p2:
        if s[p1] == s[p2]:
            p1+=1
            p2-=1
            continue
        if not (s[p1].isalpha() or s[p1].isdigit()):
            p1+=1
            continue
        if not (s[p2].isalpha() or s[p2].isdigit()):
            p2 -= 1
            continue
        return False
    return True


'''
Эталонное решение палиндрома

'''
def is_palindrome_reference(s: str) -> bool:
    l = 0
    r = len(s) - 1
    while l < r:
        # переходим к следующей букве пока l и r
        # не будут указывать на буквы или цифры
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        # оба символа - буквы или цифры
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
