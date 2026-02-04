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


'''
Маршрут туриста
средне
# решено

# яндекс
Дан набор пар городов tickets,
 где tickets[i] = [город отправления, город прибытия] в которых побывал турист.
  Нужно восстановить маршрут следования туриста.

Известно, что все города относятся к одному путешествию,
 и что каждый следующий перелёт турист начинал из того города, 
 в котором закончил предыдущий и никакой город не был посещён туристом дважды.
'''

# мое решение
def route(tickets: List[List[str]]) -> List[str]:
    finish_city = set()
    route_map = {}
    for c1, c2 in tickets:
        route_map[c1] = c2
        finish_city.add(c2)
    for city in route_map.keys():
        if city not in finish_city:
            start_city = city
    route = []
    while start_city:
        route.append(start_city)
        start_city = route_map.get(start_city)
    return route


# эталонное решение
def route(tickets: List[List[str]]) -> List[str]:
    # destination_cities - сет городов, куда прибывал турист
    destination_cities = set()
    # ключ: город отправления, значение: город прибытия
    mapping = {}
    for ticket in tickets:
        destination_cities.add(ticket[1])
        mapping[ticket[0]] = ticket[1]

    # ищем город из которого было отправление
    #  этот город ни разу не должен упоминяться как
    #  пункт прибытия
    start_city = ""
    for ticket in tickets:
        if ticket[0] not in destination_cities:
            start_city = ticket[0]
            break

    # начиная со start_city восстанавливаем маршрут
    result = [start_city]
    for _ in range(len(tickets)):
        result.append(mapping[result[-1]])
    return result


'''
Слово - анаграмма
легко
# решено

# озон

# яндекс
Даны две строки s и t, нужно вернуть true, если t является анаграммой s, и false в противном случае.

Анаграмма — это слово или фраза, образованная путем перестановки букв другого слова или фразы, с использованием всех исходных букв ровно один раз.

Пример 1:

Ввод: s="hello", t="lolhe"
Вывод: true
Пример 2:

Ввод: s="car", t="cat"
Вывод: false
Пример 3:

Ввод: s="abc", t="abcc"
Вывод: false
'''

# решение 1
def is_valid_anagram(s: str, t: str) -> bool:
    char_count_s = {}
    char_count_t = {}
    for char in s:
        char_count_s[char] = char_count_s.get(char, 0) + 1
    for char in t:
        char_count_t[char] = char_count_t.get(char, 0) + 1
    return char_count_s == char_count_t

# решение 2
def is_valid_anagram(s: str, t: str) -> bool:
    char_counter = [0 for _ in range(26)]

    for char in s:
        char_counter[ord(char) - ord('a')] += 1
    for char in t:
        char_counter[ord(char) - ord('a')] -= 1

    return char_counter == [0 for _ in range(26)]