'''
Условие
Дан массив целых чисел nums и число k. Необходимо вернуть k наиболее часто встречающихся элементов.

Ответ можно вернуть в любом порядке.

Пример
Ввод: nums = [5,7,5,6,6,5], k = 2
Вывод: [5,6]
Объяснение: элемент 5 встречается 3 раза, элемент 6 встречается 2 раза, а элемент 7 всего один, поэтому мы возвращаем 5 и 6, так как они топ 2 самых встречающихся элементов.
'''
from collections import defaultdict
from pprint import pprint
from typing import *


# простое решение за O(log(n))
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    hash_map = defaultdict(int)
    for num in nums:
        hash_map[num]+=1

    result_list = list(hash_map.items())
    result_list.sort(key = lambda x: x[1], reverse=True)
    print(result_list)
    return [item[0] for item in result_list[:k]]

# print(top_k_frequent([5,7,5,6,6,5], 2))

# мое решение после просмотра эталонного
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    hash_map = Counter(nums)
    frequency_list = [[] for i in range(len(nums) + 1)]
    for num, count in hash_map.items():
        frequency_list[count].append(num)

    result = []
    for nums in reversed(frequency_list):
        if k <=0:
            return result
        result.extend(nums[:k])
        k-=len(nums)
    return result


# эталонное решение
from typing import *

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # ключ - число, значение - сколько раз встретилось
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 0
        count[num] += 1

    # индекс массива - сколько раз встретилось число
    # значение - список чисел, которые встретились столько раз
    frequencyList = [[] for _ in range(len(nums) + 1)]
    for num in count:
        frequency = count[num]
        frequencyList[frequency].append(num)

    # допустим у нас получился такой frequencyList:
    # 0: []
    # 1: [2, 5]
    # 2: []
    # 3: [4]
    # 4: []
    # 5: []
    # при k = 1 нам нужно вернуть 4
    # для этого проходимся с конца и ищем первые k элементов
    result = []
    for numsList in reversed(frequencyList):
        for num in numsList:
            if k <= 0:
                return result
            result.append(num)
            k -= 1
    return result


from typing import *


'''
Судоку
средне
# решено
Проверь,  является ли заданная расстановка чисел в судоку размером 9 x 9 допустимой.
Массив board содержит только числа от 1 до 9 включительно.  

Условия:

Каждая строка содержит только уникальные числа.
Каждый столбец содержит только уникальные числа.
Каждый из девяти подполей 3 x 3 содержит только уникальные числа.
Примечание: 

Решать судоку не требуется. 
Необходимо просто проверить отсутствие дубликатов в строках, столбцах и подполях.
 Если дубликаты отсутствуют, вернуть true. В противном случае вернуть false.  
'''
def is_valid_sudoku(board: List[List[str]]) -> bool:
    frequency_counter = [[[0 for _ in range(10)] for _ in range(9)] for i in range(3)]

    def get_correct_counter(number: int):
        mapping = {0: 0, 3:1, 6: 2}
        return mapping.get(number)
    for i in range(0, 9, 3):  # 0, 3, 6
        chunk_lists = board[i:i + 3]
        for idx, list_numbers in enumerate(chunk_lists):  # 0, 1, 2
            for l in range(0, 9, 3):  # 0, 3, 6
                chunk_numbers = list_numbers[l:l + 3]
                for j, num in enumerate(chunk_numbers):  # 0, 1, 2
                    if not num.isdigit():
                        continue
                    if frequency_counter[0][i + idx][int(num)] == 1:
                        return False
                    frequency_counter[0][i + idx][int(num)] += 1
                    if frequency_counter[1][j + l][int(num)] == 1:
                        return False
                    frequency_counter[1][j + l][int(num)] += 1
                    if frequency_counter[2][i+get_correct_counter(l)][int(num)] == 1:
                        return False
                    frequency_counter[2][i+get_correct_counter(l)][int(num)] += 1

    return True


# эталонное решение
from typing import *

def is_valid_sudoku(board: List[List[str]]) -> bool:
    # храним пару (номер строки, значение)
    rows = set()
    # храним пару (номер колонки, значение)
    cols = set()
    # храним пару (номер блока, значение)
    blocks = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            val = board[i][j]
            if val == ".":
                continue
            blockIdx = i // 3 * 3 + j //3
            # если у нас уже есть такой элемент в строке/столбце/блоке
            # значит невалидное судоку
            if (i, val) in rows or (j, val) in cols or (blockIdx, val) in blocks:
                return False
            rows.add((i, val))
            cols.add((j, val))
            blocks.add((blockIdx, val))
    return True

'''
Соревнования по числу шaгов
средне
# решено

# авито
Недавно закончился чемпионат по шагам и тебе нужно подвести его итоги! Дан массив statistics, где statistics[i] = [[id участника, число шагов в i-ый день], ...]. Нужно вернуть id всех участников, которые прошли максимальное число шагов и одновременно с этом принимали участие в соревнованиях каждый день. Результат можно вернуть в любом порядке.

Если ни один из участников не принимал участие в соревнованиях каждый день, то нужно вернуть пустой массив.
'''
# мое решение
def find_competition_winners(statistics: List[List[List[int]]]) -> List[int]:
    competition = {key: value for key, value in statistics[0]}
    for day, statistic in enumerate(statistics[1:]):
        competition_upd = {}
        for participant_id, steps in statistic:
            if participant_id not in competition:
                continue
            competition_upd[participant_id] = steps + competition[participant_id]
        competition = competition_upd

    if not competition:
        return []
    max_steps = 0
    result = []
    for participant_id, steps in competition.items():
        if steps == max_steps:
            result.append(participant_id)
        if steps > max_steps:
            result = [participant_id]
            max_steps = steps

    return result

#
# find_competition_winners([[[2,4000],[1,500],[3,2000]],
#                           [[1,5000],[3,150],[2,1000]],
#                           [[2,3420],[1,10000],[3,12850]]])


# эталонное решение
def find_competition_winners(statistics: List[List[List[int]]]) -> List[int]:
    user_stats = {}
    # max_steps_count: максимальное число шагов среди участников, которые
    # участвовали каждый день
    max_steps_count = 0
    for day in statistics:
        for user in day:
            user_id, user_steps_count = user
            if user_id not in user_stats:
                user_stats[user_id] = [0, 0]

            # увеличиваем кол-во дней и число шагов для user_id
            days_count = user_stats[user_id][0] + 1
            steps_count = user_steps_count + user_stats[user_id][1]
            user_stats[user_id] = [days_count, steps_count]

            # обновляем max_steps_count, если было участие во всех днях
            if days_count == len(statistics):
                max_steps_count = max(max_steps_count, steps_count)

    # формируем результирующий массив из id участников
    result = []
    for user_id in user_stats:
        user_stat = user_stats[user_id]
        if user_stat[0] == len(statistics) and user_stat[1] == max_steps_count:
            result.append(user_id)
    return result


# мое решение после того, как посмотрел
def find_competition_winners(statistics: List[List[List[int]]]) -> List[int]:
    days = len(statistics)
    new_stat = {}
    max_steps = 0
    result = []
    for day, statistic in enumerate(statistics):
        for participant_id, steps in statistic:
            if participant_id not in new_stat:
                new_stat[participant_id] = [0, 0]  # steps, day
            new_stat[participant_id][0] += steps
            new_stat[participant_id][1] += 1
            if new_stat[participant_id][1] == days and new_stat[participant_id][0] == max_steps:
                result.append(participant_id)
            if new_stat[participant_id][1] == days and new_stat[participant_id][0] > max_steps:
                result = [participant_id]
                max_steps = new_stat[participant_id][0]

    return result


'''
Поиск анаграмм
средне
# решено

# яндекс
Даны строки s и t. Нужно найти все индексы в строке s,
 с которых начинается подстрока — анаграмма строки t, и вернуть их в порядке возрастания.
  Считается, что символы могут быть любыми и заранее не известны (алфавит не ограничен),
   но на практике строки будут состоять только из символов ascii.
'''
# мое решение - втупую перебор..((((
def find_anagrams(s: str, t: str) -> List[int]:
    def is_anagram(s, t):
        counter = [0 for _ in range(128)]
        for char in s:
            counter[ord(char)] += 1
        for char in t:
            counter[ord(char)] -=1
        return counter == [0 for _ in range(128)]

    result = []
    an_length = len(t)
    p = 0
    while p+len(t) <= len(s):
        if is_anagram(s[p:p+len(t)], t):
            result.append(p)
        p+=1

    return result


def find_anagrams(s: str, t: str) -> List[int]:
    hash_map = defaultdict(int)
    an_length = len(t)
    result = []
    for char in t:
        hash_map[char] += 1

    # первое окно
    for char in s[0:len(t)]:
        hash_map[char] -= 1
        if hash_map[char] == 0:
            del hash_map[char]
    if not hash_map:
        result.append(0)
    p = 1

    while p + len(t) - 1 < len(s):
        hash_map[s[p - 1]] += 1
        if hash_map[s[p-1]] == 0:
            del hash_map[s[p-1]]
        hash_map[s[p + len(t) - 1]] -= 1
        if hash_map[s[p + len(t) - 1]] == 0:
            del hash_map[s[p + len(t) - 1]]
        if not hash_map:
            result.append(p)
        p += 1
    return result


s = 'abacbaab'
t = 'aab'

find_anagrams(s, t)

'''
Строгая симметрия по оси Y
средне
# решено

# островок

# сбердевайсы

# яндекс
Дан массив точек points. Нужно вернуть true, если существует такая прямая, параллельная оси Y, которая симметрично отражает все данные точки и false, если такой прямой нет.

ВАЖНО: При этом каждая точка должна иметь симметричную ей точку в массиве с таким же числом вхождений.

Пример 1:

Ввод: points = [[1,2],[3,2]]
Вывод: true
Пример 2:

Ввод: points = [[1,2],[3,2],[2,1],[2,1]]
Вывод: true
Пример 3:

Ввод: points = [[2,3],[4,3],[3,1],[3,1]]
Вывод: true
Пример 4:

Ввод: points = [[1,1],[2,1],[2,1]]
Вывод: false
Ограничения:

1 ≤ len(points)
Каждая точка — массив из двух целых чисел [x, y]
Координаты x и y — целые числа
'''

# мое решение
def is_symmetric(points: List[List[int]]) -> bool:
    maxX = max(x for x,y in points)
    minX = min(x for x,y in points)
    hash_map = defaultdict(int)
    for x, y in points:
        if (x,y) == (maxX+minX - x, y):
            continue
        if hash_map.get((maxX+minX - x, y)):
            hash_map[(maxX+minX - x, y)] -= 1
            if hash_map[(maxX+minX - x, y)] == 0:
                del hash_map[(maxX+minX - x, y)]
        else:
            hash_map[(x, y)]+=1
    return not bool(hash_map)


# эталонное решение
def is_symmetric(points: List[List[int]]) -> bool:
    # находим минимальный и максимальный X
    maxX = max(x for x, y in points)
    minX = min(x for x, y in points)

    # ключ: координата точки, значение: кол-во точек
    points_map = {}
    for point in points:
        map_key = (point[0], point[1])
        if map_key not in points_map:
            points_map[map_key] = 0
        points_map[map_key] += 1

    for x, y in points:
        # формула: maxX + minX - x
        #  позволяет находить значение по оси X симметричной точки

        # проверяем наличие симметричной точки
        if (maxX + minX - x, y) not in points_map:
            return False
        # проверяем, что число симметричных точек совпадает
        if points_map[(maxX + minX - x, y)] != points_map[(x, y)]:
            return False
    return True



'''
Последовательность с суммой K
легко

# островок

# яндекс
Дан неотсортированный массив nums целых чисел, необходимо определить, существует ли такая непрерывная последовательность, сумма элементов которой равна k.

Нужно вернуть индекс последнего элемента первой встретившейся последовательности, иначе -1.

Пример 1:

Ввод: nums = [1, 2, 3], k = 5
Вывод: 2
Пример 2:

Ввод: nums = [1, 2, 3], k = 7
Вывод: -1
Пример 3:

Ввод: nums = [1, 2, 5, 7], k = 7
Вывод: 2
Объяснение: существует 2 непрерывных последовательности, в сумме равные 7 [2, 5] и [7] в качестве ответа возвращаем последний индекс последовательности [2, 5], так как она встретилась раньше.
Ограничения:

len(nums) >= 1
k >= 0
'''

def subsequence_sum_k(nums: List[int], k: int) -> int:
    # храним встретившиеся префиксные суммы (далее левая граница последовательности)
    hashmap = {0: 1}
    # храним текущую префиксную сумму (далее правая граница последовательности)
    current_sum = 0

    for idx, num in enumerate(nums):
        # накапливаем текущую префиксную сумму (правая граница последовательности)
        current_sum += num
        # разница между текущей префиксной суммой и суммой таргетной последовательности (потенциальная левая граница последовательности)
        difference = current_sum - k
        # проверяем, дает ли разница число k
        if difference in hashmap:
            return idx
        # сохраняем текущую сумму как потенциальную левую границу
        hashmap[current_sum] = hashmap.get(current_sum, 0) + 1

    return -1

subsequence_sum_k([1, 2, -1, 3, 1, 4], 5)


'''
Палиндром из строки
легко

# озон
Дана строка  s. Нужно определить размер самого длинного палиндрома, который можно составить из её символов.

Палиндром — это слово, которое читается слева направо и справа налево одинаково.

Реши задачу так, как будто ты не знаешь, сколько именно различных символов в строке и какие они, но точно знаешь, что их меньше 128.

Пример 1:

Ввод: s = "aaabbbccccdd"
Вывод: 11
Объяснение: "dccbaaabccd" один из примеров палиндрома
Пример 2:

Ввод: s = "abc"
Вывод: 1
Объяснение: палиндромом могут быть строки "a" или "b" или "c"
Ограничения:

len(s) >= 0
s содержит только ascii символы
'''

# мое решение
def find_palindrome_length(s: str) -> int:
    hash_map = {}
    common_count = 0
    for char in s:
        if not hash_map.get(char):
            hash_map[char] =1
        else:
            del hash_map[char]
            common_count +=2
    if hash_map:
        common_count+=1
    return common_count


# эталонное решение
from typing import *

def find_palindrome_length(s: str) -> int:
    result = 0
    chars = set()
    for ch in s:
        if ch in chars:
            chars.remove(ch)
            result += 2
        else:
            chars.add(ch)
    return result + min(1, len(chars))


'''
Максимальное произведение
легко
# решено

# озон
Дан массив nums, состоящий из положительных целых чисел. Нужно вернуть максимальное произведение двух различных элементов массива.

Пример 1:

Ввод: nums = [5,3,10,2,8,5]
Вывод: 80
Объяснение: 10 * 8 = 80
Пример 2:

Ввод: nums = [10,10,10]
Вывод: 100
Ограничения:

len(nums) >= 2
nums[i] >= 1
'''

# мое решение
def max_product(nums: List[int]) -> int:
    max1 = nums[0]
    max2 = nums[1]
    for num in nums[2:]:
        if max1 > max2 and num>max2:
            max2=num
        elif num >max1:
            max1=num
    return max1*max2


# эталонное решение
def max_product(nums: List[int]) -> int:
    m1 = max(nums[0], nums[1])
    m2 = min(nums[0], nums[1])
    for i in range(2, len(nums)):
        if nums[i] > m1:
            m2 = m1
            m1 = nums[i]
        elif nums[i] > m2:
            m2 = nums[i]

    return m1 * m2
