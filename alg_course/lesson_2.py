# Каждому по указателю.

'''
Общие элементы массивов


# яндекс
Даны два отсортированных по возрастанию массива nums1 и nums2. Необходимо вернуть новый массив nums3, который содержит все общие элементы из nums1 и nums2.

Результат должен быть также отсортирован по возрастанию. Если элементы встречаются в массивах несколько раз, то их нужно продублировать в ответе.

Пример 1:

Ввод: nums1 = [-3,2,2,5,8,19,31], nums2 = [1,2,2,2,6,19,52]
Вывод: [2,2,19]
Пример 2:

Ввод: nums1 = [-5,4], nums2 = [1,2]
Вывод: []
Пример 3:

Ввод: nums1 = [], nums2 = [1,2]
Вывод: []
Ограничения:

len(nums1), len(nums2) >= 0
'''

from typing import *

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    p1 = 0
    p2 = 0
    nums_3 = []
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            nums_3.append(nums1[p1])
            p1+=1
            p2+=1
            continue
        elif nums1[p1] <= nums2[p2]:
            p1+=1
        else:
            p2+=1
    return nums_3


'''
Неточный поиск
легко

# желтый банк

# яндекс
Даны две строки s и t. Необходимо определить, можно ли получить строку s, удаляя некоторые (возможно, ни одного) символы из строки t, не изменяя порядок оставшихся символов.

Пример 1:

Ввод: s = "abc", t = "a1b2c3"
Вывод: True
Объяснение: Можно удалить цифры из t, чтобы получить t = "abc"
Пример 2:

Ввод: s = "abc", t = "acb"
Вывод: False
Ограничения:

len(s) ≥ 0
len(t) ≥ 0
Строки s и t содержат только ascii символы
'''

from typing import *
# мое решение
def fuzzy_match(s: str, t: str) -> bool:
    p1 = 0
    p2 = 0
    while True:
        if p1>=len(s):
            return True
        if p2>=len(t):
            return False
        if s[p1] == t[p2]:
            p1+=1
            p2+=1
        else:
            p2+=1

#эталонное решение
def fuzzy_match(s: str, t: str) -> bool:
    p1, p2 = 0, 0

    # Пока не достигли конца хотя бы одной из строк
    while p1 < len(s) and p2 < len(t):
        if s[p1] == t[p2]:
            # Если символы совпадают — продвигаем указатель по s
            p1 += 1
        # Всегда двигаем указатель по t
        p2 += 1
    return p1 == len(s)


'''
Симметричная разница массивов
средне
# решено
Даны два массива nums1 и nums2, отсортированные по возрастанию и состоящие из уникальных элементов.
 Нужно найти все элементы, которые встречаются только в одном из массивов и вернуть их в порядке возрастания.

Пример 1:

Ввод: nums1 = [1,5,7,9], nums2 = [2,3,5,6,7,8]
Вывод: [1,2,3,6,8,9]
Пример 2:

Ввод: nums1 = [2,3], nums2 = [1]
Вывод: [1,2,3]
Ограничения:

len(nums1) + len(nums2) >= 1
'''

# мое решение
def find_difference(nums1: List[int], nums2: List[int]) -> List[int]:
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(nums1) or p2 < len(nums2):
        if p1 >= len(nums1):
            result.extend(nums2[p2:])
            break
        elif p2 >= len(nums2):
            result.extend(nums1[p1:])
            break
        if nums1[p1] == nums2[p2]:
            p1+=1
            p2+=1
            continue
        if nums1[p1] < nums2[p2]:
            result.append(nums1[p1])
            p1+=1
        else:
            result.append(nums2[p2])
            p2+=1
    return result


# эталонное решение
def find_difference(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    p1 = 0
    p2 = 0

    while p1 < len(nums1) or p2 < len(nums2):
        # если вышли за границу nums2, значит нужно
        #   добавить оставшиеся элементы из nums1
        if p2 >= len(nums2):
            result.append(nums1[p1])
            p1 += 1
            continue
        # если вышли за границу nums1, значит нужно
        #   добавить оставшиеся элементы из nums2
        if p1 >= len(nums1):
            result.append(nums2[p2])
            p2 += 1
            continue

        # меньшее значение добавляем в ответ, а если
        #  указатели равны, то двигаем оба указателя
        if nums1[p1] < nums2[p2]:
            result.append(nums1[p1])
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            result.append(nums2[p2])
            p2 += 1
        else:
            p1 += 1
            p2 += 1
    return result