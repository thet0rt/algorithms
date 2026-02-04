from typing import *

def two_sum(nums: list[int], target: int):
    used_nums = {}
    for idx, first_num in enumerate(nums):
        second_num = target-first_num
        if second_num in used_nums:
            return [used_nums[second_num], idx]
        used_nums[first_num] = idx
    return []



# target = -1
# [1, 4, 3, -6, 2, 5]

'''
Наличие повторений
легко

# левел.тревел
Дан массив целых чисел nums, верни true,
если любое значение встречается хотя бы два раза, и верни false, если все элементы уникальны.
'''

def contains_duplicate(nums: List[int]) -> bool:
    return not len(set(nums)) == len(nums)


'''
Изоморфные строки
средне
# решено

# яндекс
Даны две строки s, t и нужно вернуть true если они изоморфны и false в обратном случае.

Строки s и t изоморфны, если символы в s можно заменить так, чтобы получить t.

ВАЖНО: каждый символ в строке должен быть заменен другим символом , при этом порядок символов должен сохраняться. Разные символы не могут заменяться на один и тот же, но символ может оставаться неизменным.
'''

# мое решение
def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    hash_map = {}
    used = set()
    for idx, char in enumerate(s):
        if char not in hash_map:
            if t[idx] in used:
                return False
            hash_map[char] = t[idx]
            used.add(t[idx])
        elif hash_map[char] != t[idx]:
            return False
    return True


# эталонное решение
def is_isomorphic(s: str, t: str) -> bool:
    # s_map: ключ - символ из строки s,
    #  значение - соответствие с символом из строки t
    # t_map: ключ - символ из строки t,
    #  значение - соответствие с символом из строки s
    s_map, t_map = {}, {}
    for i in range(len(s)):
        # если текущий символ s[i] уже встречался раньше, то
        #  проверяем, что он соответствует тому же символу из
        #  строки t, что и в прошлый раз
        if s[i] in s_map and s_map[s[i]] != t[i]:
            return False
        # аналогичная проверка для строки t необходима, чтобы учесть условие,
        #  что ни один символ не может соответствовать 2-ум разным (даже для строки t)
        if t[i] in t_map and t_map[t[i]] != s[i]:
            return False
        # запоминаем, сопоставление символов для строк s и t
        s_map[s[i]] = t[i]
        t_map[t[i]] = s[i]
    return True