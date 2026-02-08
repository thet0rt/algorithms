from collections import defaultdict
from sys import prefix
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

'''
Сортировка 012
легко
# решено

# озон
Дан массив colors, элементы которого представляют один из трех цветов:
 красный (0), зелёный (1) и синий (2). Необходимо отсортировать массив так,
  чтобы цвета шли в порядке: красный, зелёный, синий, и вернуть изменённый массив.

Важно, чтобы сортировка осуществлялась in-place,
 что означает выполнение сортировки без использования дополнительной памяти для копий массива.
'''

# мое решение
def sort_012(colors: List[int]) -> List[int]:
    p = 0
    hash_map = {0: 0, 1: 0, 2: 0}
    for idx, color in enumerate(colors):
        hash_map[color] = hash_map.get(color, 0) + 1

    for i in range(0, 3):
        for j in range(hash_map[i]):
            colors[p] = i
            p += 1
    return colors


# эталонное решение
def sort_012(colors: List[int]) -> List[int]:
    # индекс: число, значение: кол-во повторений
    count = [0 for _ in range(3)]
    # делаем подсчет
    for num in colors:
        count[num] += 1

    # сортируем
    i = 0
    for j in range(3):
        for _ in range(count[j]):
            colors[i] = j
            i += 1
    return colors


'''
Группировка анаграмм
средне
# решено

# яндекс
Дан массив строк strs и нужно сгруппировать анаграммы вместе. Ответ можно вернуть в любом порядке.

Анаграмма — это слово или фраза, образованная путем перестановки букв другого слова или фразы, с использованием всех исходных букв ровно один раз.
'''

# мое решение - плохонькое.. :(
def group_anagrams(strs: List[str]) -> List[List[str]]:
    def is_anagram(s, t):
        if len(s) != len(t):
            return False
        char_count = [0 for i in range(26)]
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        for char in t:
            char_count[ord(char) - ord('a')] -= 1
        return char_count == [0 for i in range(26)]

    p1 = 0
    anagrams_grouped = []
    used = set()
    while p1 < len(strs):
        word = strs[p1]
        if word in used:
            p1 += 1
            continue
        anagrams = [word]
        p2 = p1 + 1
        used.add(word)
        while p2 < len(strs):
            word_2 = strs[p2]
            if is_anagram(word, word_2):
                used.add(word_2)
                anagrams.append(word_2)
            p2 += 1
        anagrams_grouped.append(anagrams)
        p1 += 1
    return anagrams_grouped


# эталонное решение
def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)
    for aragram in strs:
        # индекс - соответствует букве (0 - 'a', 1 - 'b', ...)
        #  значение - сколько раз встретили букву
        count_chars = [0 for j in range(26)]
        for ch in aragram:
            count_chars[ord(ch) - ord('a')] += 1

        # добавляем анаграмму группу
        anagram_groups[tuple(count_chars)].append(aragram)

    return list(anagram_groups.values())


'''
Перестановка букв
средне
# решено

# яндекс
Дана строка s. Нужно вернуть true, если после перестановки символов в строке может получится палиндром, и false в противном случае.

Палиндром — это строка, которая читается одинаково слева направо и справа налево.
'''

# мое решение
def is_palindrome_permutation(s: str) -> bool:
    char_counter = [0 for _ in range(26)]
    for char in s:
        char_counter[ord(char) - ord('a')] += 1
    odd = 0
    for count in char_counter:
        if count % 2 != 0:
            odd+=1
        if odd>1:
            return False
    return True

# эталонное решение
def is_palindrome_permutation(s: str) -> bool:
    # слово можно сделать палиндромом при условии, что каждая буква
    #  встречается четное кол-во раз или же только 1 буква нечетное число раз

    # индекс - соответствует букве (0 - 'a', 1 - 'b', ...)
    #  значение - 0 будет означать, что у буквы пара есть/мы не встретили букву
    #  (нам не нужно для решения задачи резличать эти случаи)
    #  значение - 1, что у буква встретилась нечетное число раз
    count = [0 for _ in range(26)]
    for char in s:
        # ord(char) - ord('a') - позволяет перевести 'a' -> 0, 'b' -> 1 и т д

        # подсчитываем четность с которой встречали букву
        count[ord(char) - ord('a')] = (count[ord(char) - ord('a')] + 1) % 2

    # если 1 или 0 букв встречается нечетное число раз - значит можно сделать палиндром
    return sum(count) <= 1


'''
Условие
Даны два целочисленных массива nums1 и nums2 длины n. Оба массива содержат только числа от 1 до n включительно, при этом каждое число обязательно встречается ровно один раз в каждом из массивов.  

Нужно найти общий префиксный массив для nums1 и nums2.  

Пример
Ввод: nums1 = [2,1,3,4,5], nums2 = [3,1,2,5,4]
Вывод: [0,1,3,3,5]
Объяснение:
0 = [2] и [3] имеют 0 общих элементов
1 = [2,1] и [3,1] имеют 1 общий элемент (1)
3 = [2,1,3] и [3,1,2] имеют 3 общих элемента (1,2,3)
3 = [2,1,3,4] и [3,1,2,5] имеют 3 общих элемента (1,2,3)
5 = [2,1,3,4,5] и [3,1,2,5,4] имеют 5 общих элементов (1,2,3,4,5)

'''

# мое решение - не очень хорошо из-за prefix_list.append(sum(hash_map.values()))
# тк тут каждый раз мы проходимся по всему списку, будет n^2
def find_common_prefix(nums1: List[int], nums2: List[int]) -> List[int]:
    p = 0
    hash_map = {}
    prefix_list = []
    while p < len(nums1):
        if nums1[p] in hash_map:
            hash_map[nums1[p]] = 1
        else:
            hash_map[nums1[p]] = 0
        if nums2[p] in hash_map:
            hash_map[nums2[p]] = 1
        else:
            hash_map[nums2[p]] = 0
        prefix_list.append(sum(hash_map.values()))
        p+=1
    return prefix_list


# print(find_common_prefix([2,1,3,4,5], [3,1,2,5,4]))

#эталонное решение через хэш-таблицу
from typing import *
from collections import defaultdict

#Время: O(n), где n — размер входного массива. Линейная сложность, так как каждый
#элемент проходит через цикл.
#Память: O(n), где n — размер входного массива. Для подсчета мы используем хеш-таблицу,
#а для результата — массив.
def find_common_prefix(nums1: List[int], nums2: List[int]) -> List[int]:
    n = len(nums1)
    prefix_common_array = [0] * n

    # Используем defaultdict для подсчета количества встреченных элементов
    count_map = defaultdict(int)
    common_count = 0

    for current_index in range(n):
        # Ключ здесь элемент массива, а значение - количество повторений
        count_map[nums1[current_index]] += 1

        # Если элемент из nums1 уже встречался в nums2, увеличиваем общий счетчик
        if count_map[nums1[current_index]] == 2:
            common_count += 1

        count_map[nums2[current_index]] += 1

        # Если элемент из nums2 уже встречался в nums1, увеличиваем общий счетчик
        if count_map[nums2[current_index]] == 2:
            common_count += 1

        # Сохраняем количество общих элементов на текущем индексе
        prefix_common_array[current_index] = common_count

    return prefix_common_array


# мое через массив (после того, как уже посмотрел)
def find_common_prefix(nums1: List[int], nums2: List[int]) -> List[int]:
    n = len(nums1)
    counter = [0 for _ in range(n)]
    p = 0
    common_counter = 0
    result = []
    while p < len(nums1):
        counter[nums1[p]-1]+=1
        if counter[nums1[p]-1] == 2:
            common_counter +=1
        counter[nums2[p]-1]+=1
        if counter[nums2[p]-1] == 2:
            common_counter+=1
        result.append(common_counter)
        p+=1
    return result

# print(find_common_prefix([2,1,3,4,5], [3,1,2,5,4]))

# эталонное решение через массив
from typing import *

#Время: O(n), где n — размер входного массива. Линейная сложность, так как каждый
#элемент проходит через цикл.
#Память: O(n), где n — размер входного массива. Для подсчета мы используем хеш-таблицу,
#а для результата — массив.
def find_common_prefix(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    frequency = [0] * (len(nums1) + 1)

    common = 0
    for i in range(len(nums1)):
        frequency[nums1[i]] += 1
        frequency[nums2[i]] += 1

        # если общий элемент, то +1 к общим элементам на префиксе
        if nums1[i] == nums2[i]:
            common += 1
            result.append(common)
            continue

        # если до этого уже встречали nums1[i], то +1
        if frequency[nums1[i]] == 2:
            common += 1
        # если до этого уже встречали nums2[i], то +1
        if frequency[nums2[i]] == 2:
            common += 1

        result.append(common)
    return result


