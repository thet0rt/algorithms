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


'''
Дан список s, представляющий URL-адрес (буквы и пробелы). Нужно заменить все пробелы в первых k символах на %20, используя свободное место в конце списка и вернуть изменённый список s в качестве ответа.

Пример 1:

Ввод: s = ["h","e","l","l","o"," ","w","o","r","l","d","#","#"], k = 11
Вывод: ["h","e","l","l","o","%","2","0","w","o","r","l","d"]
Пример 2:

Ввод: s = ["a"," ","b"," ", " ", "c","#","#","#","#","#","#"], k = 6
Вывод: ["a","%","2","0","b","%","2","0","%","2","0", "c"]
Ограничения:

len(s) >= 1
k <= len(s)
s всегда имеет достаточно места для размещения
'''

from typing import *

# мое решение
def urlify(s: List[str], k: int) -> List[str]:
    p1 = 0
    p2 = len(s) - 1
    while p1 < k:
        if s[p1] != ' ':
            p1 += 1
            continue
        rasst = p2 - p1-1
        s[p1] = '%'
        for i in range(2):
            print(i)
            p3 = p2
            for j in range(rasst):
                s[p3], s[p3-1] = s[p3-1], s[p3]
                p3-=1
            if i == 0:
                s[p3] = '0'
            else:
                s[p3] = '2'
        p1+=1
        k+=2
    return s

# print(urlify(["h","e","l","l","o"," ","w","o","r","l","d","#","#"], 11))
# print(urlify(["a"," ","b"," ", " ", "c","#","#","#","#","#","#"], 6))

from typing import *

# эталонное решение
def urlify(s: List[str], k: int) -> List[str]:
    # медленный указатель - куда ставим символ
    slow = len(s) - 1
    # быстрый указатель - откуда берем символ
    fast = k - 1

    while fast >= 0:
        # если символ не пробел, то
        #  дублируем значение на новое место
        if s[fast] != " ":
            s[slow], s[fast] = s[fast], s[slow]
            slow -= 1
            fast -= 1
            continue

        # если символ пробел, заменяем его на %20
        s[slow - 2] = "%"
        s[slow - 1] = "2"
        s[slow] = "0"
        slow -= 3
        fast -= 1
    return s

# urlify(["h","e","l","l","o"," ","w","o","r","l","d","#","#"], 11)
# urlify(["a"," ","b"," ", " ", "c","#","#","#","#","#","#"], 6)
# urlify(["h","e","l","l","o"," ","#","#","w","o","r","l","d"], 11)
'''
Декодирование URL-адреса
средне
# решено

# вк
Дан список s. Нужно заменить все вхождения %20 на пробелы в списке s, а оставшиеся лишние символы заменить на #, сохранив длину списка. В качестве ответа верни изменённый список s.

Пример 1:

Ввод: s = ["h","e","l","l","o","%","2","0","w","o","r","l","d"]
Вывод: ["h","e","l","l","o"," ","w","o","r","l","d","#","#"]
Пример 2:

Ввод: s = ["a","%","2","0","b","%","2","0","%","2","0", "c"]
Вывод: ["a"," ","b"," ", " ", "c","#","#","#","#","#","#"]
Ограничения:

len(s) >= 1
'''
# мое решение
def unurlify(s: List[str]) -> List[str]:
    slow = 0
    fast = 0
    while fast < len(s):
        print(s)
        if s[fast] != '%':
            s[slow], s[fast] = s[fast], s[slow]
            slow +=1
            fast +=1
            continue
        s[fast] = ' '
        s[fast+1] = '#'
        s[fast+2] = '#'
        s[slow], s[fast] = s[fast], s[slow]
        fast += 3
        slow +=1
    print(s)
    return s

# s = ["h","e","l","l","o","%","2","0","w","o","r","l","d"]
#
# unurlify(s)
# unurlify(["a","%","2","0","b","%","2","0","%","2","0", "c"])

# эталонное решение
def unurlify(s: List[str]) -> List[str]:
    # медленный указатель - куда ставим символ
    slow = 0
    # быстрый указатель - откуда берем символ
    fast = 0

    while fast < len(s):
        # если встречаем %20, то заменяем на пробел
        if fast + 2 < len(s) and s[fast] == "%" and s[fast + 1] == "2" and s[fast + 2] == "0":
            s[slow] = " "
            slow += 1
            fast += 3
            continue

        # если нет последовательности %20, то копируем символ
        s[slow] = s[fast]
        slow += 1
        fast += 1

    # затираем лишние символы
    for i in range(slow, len(s)):
        s[i] = "#"
    return s

'''
Удаление дубликатов 2
легко

# озон
Пример 1:

Дан массив nums, состоящий из целых чисел. Требуется изменить исходный массив, удалив все дубликаты элементов так, чтобы осталось только первое вхождение каждого уникального значения. Порядок оставшихся элементов должен сохраниться.

В качестве результата верните измененный массив nums.

Ввод: nums = [3,2,1,1,0,4,5,2,0]
Вывод: [3,2,1,0,4,5]
Пример 2:

Ввод: nums = [1,1,1,1]
Вывод: [1]
Ограничения

len(nums) >= 0
'''

# мое решение
def remove_duplicates(nums: List[int]) -> List[int]:
    p = 0
    hash_map = set()
    length = len(nums)
    while p<len(nums):
        if nums[p] in hash_map:
            del nums[p]
            length-=1
            continue
        hash_map.add(nums[p])
        p+=1
    return nums


# эталонное решение
def remove_duplicates(nums: List[int]) -> List[int]:
    p1 = 0
    p2 = 0
    used = set()
    while p2 < len(nums):
        if nums[p2] not in used:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1+=1
        used.add(nums[p2])
        p2+=1
    return nums[:p1-1]

# print(remove_duplicates([3,2,1,1,0,4,5,2,0]))
'''
Поиск дубликата
средне

# озон
Дан массив nums, содержащий n + 1 чисел, каждое из которых находится в диапазоне от 1 до n. Требуется найти число, которое повторяется более одного раза. Нельзя модифицировать массив или использовать дополнительную память.

Пример 1:

Ввод: nums = [3,1,3,4,2]
Вывод: 3
Пример 2:

Ввод: nums = [1,1]
Вывод: 1
Ограничения:

len(nums) >= 2
1 <= nums[i] <= len(nums)
'''




def find_duplicate_num(nums: List[int]) -> int:
    slow = 0
    fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow=0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

# find_duplicate_num([1, 4, 6, 2, 6, 3, 5])



'''
Минимальная разность
легко

# дзен

# желтый банк

# яндекс
Даны два массива целых чисел nums1 и nums2. Найдите минимальное значение выражения |a - b|, где a — элемент nums1, b — элемент nums2.

Пример 1:

Ввод: nums1 = [1,15,3], nums2 = [21,10,30]
Вывод: 5
Объяснение: |15 - 10| = 5
Пример 2:

Ввод: nums1 = [-5,0,6], nums2 = [10,-2,3]
Вывод: 2
Объяснение: |0 - (-2)| = 2
Ограничения:

len(nums1) >= 1
len(nums2) >= 1

Оценка сложности

Время: O(n*log(n) + m*log(m)), где n - размер nums1, m - размер nums2
Память: O(1)


'''

#мое решение
def find_difference(nums1: List[int], nums2: List[int]) -> int:
    nums1.sort()
    nums2.sort()

    p1 = 0
    p2 = 0
    result = abs(nums1[0] - nums2[0]) # 9
    while p1<len(nums1) and p2<len(nums2):
        if nums1[p1] == nums2[p2]:
            return 0
        new_result = nums1[p1] - nums2[p2]
        if new_result <0:
            p1+=1
        else:
            p2+=1
        if abs(new_result) < result:
            result = abs(new_result)
    return result

# эталонное решение
def find_difference(nums1: List[int], nums2: List[int]) -> int:
    nums1.sort()
    nums2.sort()

    p1 = 0
    p2 = 0
    min_diff = abs(nums1[p1] - nums2[p2])

    while p1 < len(nums1) and p2 < len(nums2):
        diff = abs(nums1[p1] - nums2[p2])
        min_diff = min(min_diff, diff)

        if nums1[p1] < nums2[p2]:
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            return 0

    return min_diff

'''
Удаление повторов
легко

# озон
Дан массив целых чисел nums, отсортированный в неубывающем порядке. Удалите из него все дубликаты так, чтобы каждый элемент встречался только один раз. Изменения выполняйте в исходном массиве, не создавая новый. Верните изменённый массив, отсортированный по возрастанию.

Пример 1:

Ввод: nums = [1,1,2,2,3,3,4]
Вывод: [1,2,3,4]
Пример 2:

Ввод: nums = [1,1,1,1]
Вывод: [1]
Пример 3:

Ввод: nums = [10]
Вывод: [10]
Ограничения:

len(nums) >= 1
'''

# мое решение
def remove_duplicates(nums: List[int]) -> List[int]:
    used = set()
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] not in used:
            used.add(nums[fast])
            nums[slow], nums[fast] = nums[fast], nums[slow]
            fast+=1
            slow+=1
        else:
            fast+=1
    return nums[:slow]

# эталонное решение
def remove_duplicates(nums: List[int]) -> List[int]:
    # Медленный и быстрый указатели
    p1: int = 0
    p2: int = 1

    while p2 < len(nums):
        if nums[p2] != nums[p1]:
            p1 += 1
            nums[p1] = nums[p2]
        p2 += 1
    # удаляем лишние элементы без выделения дополнительной памяти
    del nums[p1 + 1:]
    return nums

'''
Похожие строки
средне

# яндекс
Даны две строки s и t. Строки считаются похожими, если они уже равны или могут стать равными после ровно одного изменения: вставки, удаления или замены одного символа. Нужно вернуть true, если строки похожи, иначе — false.

Пример 1:

Ввод: s = "iq", t = "ieq"
Вывод: true
Объяснение: можно добавить один символ и получить равные строки s = t
Пример 2:

Ввод: s = "qwe", t = "qwe"
Вывод: true
Пример 3:

Ввод: s = "abcd", t = "abcdef"
Вывод: false
Объяснение: Необходимо добавить два символа, чтобы строки стали равны.
Ограничения:

len(s) >= 0
len(t) >= 0
'''

# мое решение
def is_similar(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
        return False
    p1 = 0
    p2 = 0
    errors = 0
    while p1 < len(s) and p2 < len(t):
        if errors > 1:
            return False
        if s[p1] != t[p2]:
            errors+=1
            if len(s) > len(t):
                p1+=1
            elif len(t) > len(s):
                p2+=1
            else:
                p1+=1
                p2+=1
        else:
            p1+=1
            p2+=1
    if errors <=1:
        return True
    return False


# эталонное решение
def find_missmatch(p1: int, s: str, p2: int, t: str) -> List[int]:
    # Ищем первую позицию, где строки s и t различаются
    while p1 < len(s) and p2 < len(t):
        if s[p1] != t[p2]:
            return [p1, p2]
        p1 += 1
        p2 += 1
    return [p1, p2]

def is_similar(s: str, t: str) -> bool:
    # Строки считаются похожими, если равны или отличаются ровно на одно изменение:
    # замену, удаление или вставку одного символа
    if s == t:
        return True
    if abs(len(s) - len(t)) > 1:
        return False

    p1, p2 = find_missmatch(0, s, 0, t)

    if len(s) == len(t):
        return find_missmatch(p1 + 1, s, p2 + 1, t) == [len(s), len(t)]
    if len(s) > len(t):
        return find_missmatch(p1 + 1, s, p2, t) == [len(s), len(t)]
    return find_missmatch(p1, s, p2 + 1, t) == [len(s), len(t)]

'''
Общий префикс
легко

# яндекс
Дан массив строк strs. Нужно вернуть самую длинную строку, которая является префиксом всех строк из strs. Если общего префикса нет, верни пустую строку "".

Пример 1:

Ввод: strs = ["present","predicate","prepare"]
Вывод: "pre"
Пример 2:

Ввод: strs = ["dog","cat","bike"]
Вывод: ""
Объяснение: нет общего префикса.
Ограничения:

len(strs) >= 1
len(strs[i]) >= 1
'''

# мое решение
def longest_common_prefix(strs: List[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    prefix = strs[0]
    for word in strs[1:]:
        p = 0
        len_prefix = min(len(prefix), len(word))
        prefix = prefix[:len_prefix]
        while p < len_prefix:
            if prefix[p] != word[p]:
                prefix = prefix[:p]
                break
            p+=1
    return prefix


# эталонное решение
def longest_common_prefix(strs: List[str]) -> str:
    # Определяем минимальную длину строки среди всех
    min_len = len(strs[0])
    for el in strs:
        min_len = min(min_len, len(el))

    # Проверяем совпадение символов на каждой позиции до min_len
    for i in range(min_len):
        ch = strs[0][i]
        for el in strs:
            if ch != el[i]:
                return el[:i]

    # Все символы совпадают на отрезке длины min_len
    return strs[0][:min_len]

'''
Сумма отклонений
средне

# авито
Даны два массива целых чисел: nums1 и nums2. Для каждого элемента из nums2 найдите ближайшее по значению число в массиве nums1 и вычислите модуль разности между ними. Верните сумму всех этих разностей.

Пример 1:

Ввод: nums1 = [9,3,6,100], nums2 = [3,8,7]
Вывод: 2
Объяснение:
Для числа 3 ближайшее 3 (|3 - 3| = 0)
Для числа 8 ближайшее 9 (|8 - 9| = 1)
Для числа 7 ближайшее 6 (|7 - 6| = 1)
Ответ: 0 + 1 + 1 = 2
Пример 2:

Ввод: nums1 = [50], nums2 = [10,20,30,40]
Вывод: 100
Ограничения:

len(nums1) ≥ 1
len(nums2) ≥ 1
'''

# мое решение
def find_minimum(nums1: List[int], nums2: List[int]) -> int:
    nums1.sort()
    nums2.sort()
    p1 = 0
    p2 = 0
    full_sum = 0
    while p2 < len(nums2):
        while p1+1 < len(nums1):
            sum1 = abs(nums2[p2] - nums1[p1])
            sum2 = abs(nums2[p2] - nums1[p1+1])
            if sum1 < sum2:
                break
            p1+=1
        sum1 = abs(nums2[p2] - nums1[p1])
        full_sum += sum1
        p2+=1
    return full_sum


# эталонное решение
def find_minimum(nums1: List[int], nums2: List[int]) -> int:
    # Сортируем оба массива
    nums1.sort()
    nums2.sort()

    p1 = 0
    p2 = 0
    total = 0

    # Для каждого элемента nums2 находим ближайший в nums1
    while p2 < len(nums2):
        if p1 < len(nums1) - 1 and abs(nums2[p2] - nums1[p1]) > abs(nums2[p2] - nums1[p1 + 1]):
            p1 += 1
        else:
            # Добавляем минимальную разницу
            total += abs(nums2[p2] - nums1[p1])
            p2 += 1

    return total


is_similar('egg', 'egga')

'''
Почти палиндром
средне
# решено

# островок

# яндекс
Дана строка s. Нужно вернуть true, если из неё можно удалить не более одного символа, чтобы получился палиндром, и false — в противном случае.

Палиндром — это слово или фраза, которые читаются одинаково слева направо и справа налево.
'''
# мой вариант
def is_almost_palindrome(s: str) -> bool:
    p1 = 0
    p2 = len(s) - 1
    errors = 0
    while p1 < p2:
        if errors > 1:
            return False
        if s[p1] != s[p2]:
            errors += 1
            if s[p1+1] == s[p2]:
                p1+=1
                continue
            elif s[p2-1] == s[p1]:
                p2-=1
                continue
            else:
                return False
        p1+=1
        p2-=1
    return True


# эталонный вариант
# Проверяет, является ли подстрока s[l..r] палиндромом
def is_substring_palindrome(s: str, l: int, r: int) -> bool:
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def is_almost_palindrome(s: str) -> bool:
    for l, r in zip(range(len(s)), reversed(range(len(s)))):
        if l >= r:
            break
        if s[l] != s[r]:
            # Пробуем удалить символ либо слева, либо справа
            return is_substring_palindrome(s, l + 1, r) or \
                   is_substring_palindrome(s, l, r - 1)
    # Строка уже палиндром
    return True


'''
Сжатие пробелов
легко

# островок

# яндекс
Дан массив символов chars. Замените все подряд идущие пробелы (в том числе в начале и в конце) на один пробел. Все изменения должны быть внесены в исходный массив (без создания нового). Верните изменённый массив.

'''

# мое решение
def compress_spaces(chars: List[str]) -> List[str]:
    slow = 0
    fast = 0
    move_space = True
    while fast < len(chars):
        if chars[fast] != ' ':
            chars[slow], chars[fast] = chars[fast], chars[slow]
            move_space = True
            slow+=1

        elif move_space:
            chars[slow], chars[fast] = chars[fast], chars[slow]
            move_space=False
            slow+=1
        else:
            pass
        fast+=1
    return chars[:slow]

# compress_spaces(['a', ' ', ' ', 'b', ' ', 'c', ' ', ' ', ' '])

# эталонное решение
def compress_spaces(chars: List[str]) -> List[str]:
    slow: int = 0
    fast: int = 0
    spaces: int = 0

    while fast < len(chars):
        c = chars[fast]
        spaces = spaces + 1 if c == ' ' else 0

        if spaces <= 1:
            # Меняем элементы местами
            chars[slow], chars[fast] = chars[fast], chars[slow]
            slow += 1
        fast += 1

    return chars[:slow]

