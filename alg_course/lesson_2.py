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


'''
Односторонняя разница
легко
# решено

# яндекс
Даны два массива nums1 и nums2, отсортированные по возрастанию.

Необходимо вернуть все элементы из nums1, которые не встречаются в nums2, в отсортированном по возрастанию порядке.

Пример 1:

Ввод: nums1 = [1,2,3,4,5], nums2 = [4,5,6]
Вывод: [1,2,3]
Пример 2:

Ввод: nums1 = [1,2,2,3,3,4], nums2 = [0,0,0,3]
Вывод: [1,2,2,4]
Ограничения:

len(nums1) >= 0
len(nums2) >= 0
'''

# мое решение
def find_difference(nums1: List[int], nums2: List[int]) -> List[int]:
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(nums1):
        if p2 >= len(nums2):
            result.extend(nums1[p1:])
            break
        if nums1[p1] < nums2[p2]:
            result.append(nums1[p1])
            p1+=1
        elif nums1[p1] > nums2[p2]:
            p2+=1
        else:
            p1+=1
    return result


#эталонное решение
def find_difference(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    p1 = 0
    p2 = 0

    while p1 < len(nums1):
        # если nums2 закончился — все оставшиеся из nums1 идут в результат
        if p2 >= len(nums2):
            result.append(nums1[p1])
            p1 += 1
            continue

        # если текущий элемент nums1 меньше — он есть только в nums1
        if nums1[p1] < nums2[p2]:
            result.append(nums1[p1])
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            # при равных элементах пропускаем в nums1
            # для верной обработки дублей в nums1
            p1 += 1
    return result

'''
Хитрое сравнение строк
сложно
# решено

# желтый банк

# озон
Даны строки s и t. Нужно вернуть true в случае, если строки будут одинаковыми после ввода в текстовый редактор. Символ # в текстовом редакторе означает, что предыдущий символ нужно стереть, а если перед # отсутствует символ, то стирать ничего не нужно.

Пример 1:

Ввод: s = "ac#b#ac", t = "abc##aa#b#c"
Вывод: true
Объяснение: "aac" = "aac"
Пример 2:

Ввод: s = "a#####b", t = "b"
Вывод: true
Объяснение: "b" = "b"
Пример 3:

Ввод: s = "abcd", t = "abcd#"
Вывод: false
'''

# моё решение
def compare(s: str, t: str) -> bool:
    p1 = len(s) - 1
    p2 = len(t) - 1
    p1_skip = 0
    p2_skip = 0
    while p1 >= 0 or p2 >= 0:
        if p1>=0 and s[p1] == '#':
            p1_skip += 1
            p1-=1
            continue
        if p2>=0 and t[p2] == '#':
            p2_skip += 1
            p2-=1
            continue
        if p1_skip > 0:
            if s[p1] == '#':
                p1_skip-=1
                continue
            p1-=1
            p1_skip -= 1
            continue
        if p2_skip > 0:
            if t[p2] == '#':
                p2_skip-=1
                continue
            p2-=1
            p2_skip-=1
            continue
        if p1 < 0 or p2 < 0:
            return False
        if s[p1] != t[p2]:
            return False
        p1-=1
        p2-=1
    return True

#эталонное решение
def findNextNonSkip(s: str, i: int) -> int:
    skipCount = 0
    while i >= 0 and (skipCount > 0 or s[i] == '#'):
        if s[i] == '#':
            skipCount += 1
            i -= 1
            continue
        skipCount -= 1
        i -= 1
    return i

def compare(s: str, t: str) -> bool:
    p1, p2 = len(s), len(t)
    while p1 > 0 and p2 > 0:
        p1 = findNextNonSkip(s, p1 - 1)
        p2 = findNextNonSkip(t, p2 - 1)
        if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
            return False
    return findNextNonSkip(s, p1 - 1) == findNextNonSkip(t, p2 - 1)


# альтернативное эталонное решение
def compare(s: str, t: str) -> bool:
    p1 = len(s) - 1
    p2 = len(t) - 1
    p1_hashtag_counter = 0
    p2_hashtag_counter = 0

    def char_at(st: str, i: int):
        return st[i] if 0 <= i < len(st) else None

    while p1 >= 0 or p2 >= 0:
        if p1 >= 0 and s[p1] == '#':
            p1_hashtag_counter += 1
            p1 -= 1
            continue

        if p2 >= 0 and t[p2] == '#':
            p2_hashtag_counter += 1
            p2 -= 1
            continue

        if p1 >= 0 and s[p1] != '#' and p1_hashtag_counter > 0:
            p1 -= 1
            p1_hashtag_counter -= 1
            continue

        if p2 >= 0 and t[p2] != '#' and p2_hashtag_counter > 0:
            p2 -= 1
            p2_hashtag_counter -= 1
            continue

        if p1 >= 0 and p2 >= 0 and s[p1] == t[p2]:
            p1 -= 1
            p2 -= 1
        else:
            return False
    return True