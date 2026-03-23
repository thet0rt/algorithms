'''
Осадки в виде фрикаделек
легко
# решено
С неба падают фрикадельки, оставляя следы ДНК. Дан массив gene из строчных букв и число k. Найдите долю всех подряд идущих подстрок длины k, в которых все символы различны. Это поможет оценить вероятность новых фрикаделек в ближайшие 24 часа.

Пример 1:

Ввод: gene = "ababcdaa", k = 3
Вывод: 0.5
Объяснение: все непрерывные подстроки длины 3: ["aba", "bab", "abс", "bсd", "сda", "daa"], а без повторений: ["abс", "bсd", "сda"], а значит ответ 3/6 = 0.5
Пример 2:

Ввод: gene = "ab", k = 5
Вывод: 0
Объяснение: если строка меньше длины 5, то нельзя рассчитать вероятность на данный момент
Пример 3:

Ввод: gene = "ab", k = 1
Вывод: 1
Ограничения:

len(gene) ≥ 0
k ≥ 1
'''

# мое решение
def chance_of_meatball_precipitations(gene: str, k: int) -> float:
    if k > len(gene):
        return 0.0

    counter = [0 for i in range(26)]
    for i in range(k):
        counter[ord(gene[i]) - ord('a')] += 1
    unique_sequence = 0 if any([i > 1 for i in counter]) else 1
    all_substrings = 1
    l = 0
    r = k
    while r < len(gene):
        all_substrings +=1
        counter[ord(gene[l]) - ord('a')] -= 1
        counter[ord(gene[r]) - ord('a')] += 1
        if not any([i > 1 for i in counter]):
            unique_sequence +=1
        l+=1
        r+=1
    return unique_sequence/all_substrings


# эталонное решение
from typing import *
from collections import defaultdict


def chance_of_meatball_precipitations(gene: str, k: int) -> float:
    # k - размер плавающего окна
    if len(gene) < k:
        return float(0)

    # ключ: буква, значение: число повторов
    windowGene = defaultdict(int)
    for i in range(k):
        windowGene[gene[i]] += 1

    # result - число окон размером k с уникальными символами
    # обновляем ответ если самое первое плавающее окно содержит k уникальных символа
    result = int(len(windowGene) == k)

    # на каждом шаге цикла сдвигаем плавающее окно вправо на один
    for i in range(k, len(gene)):
        # gene[i - k] - ген, который выходит из плаваюшего окна
        windowGene[gene[i - k]] -= 1
        if windowGene[gene[i - k]] == 0:
            del windowGene[gene[i - k]]

        # gene[i] - ген, который добавляем в плавающее окно
        windowGene[gene[i]] += 1

        # обновляем ответ
        result += int(len(windowGene) == k)
    # считаем вероятность
    return float(result) / (len(gene) - k + 1)


# написал сам после просмотра ответа
def chance_of_meatball_precipitations(gene: str, k: int) -> float:
    if k > len(gene):
        return 0.0

    counter = defaultdict(int)

    for i in range(k):
        counter[gene[i]] += 1

    unique_sequence = 0 if len(counter) != k else 1
    l = 0
    r = k
    all_substrings = 1
    while r < len(gene):
        all_substrings += 1
        counter[gene[l]] -= 1
        counter[gene[r]] += 1
        if counter[gene[l]] == 0:
            del counter[gene[l]]
        if len(counter) == k:
            unique_sequence += 1
        l += 1
        r += 1

    return unique_sequence / all_substrings


'''
Инвестор в стране дураков
средне
# решено

# яндекс
В стране дураков вместо сложения используют умножение и богатый инвестор хочет этим воспользоваться, чтобы заработать и выкупить k подряд идущих домов.

Дан массив price и число k. Найдите произведения всех подряд идущих участков длины k. Массив price — цены домов, если price[i] ≤ 0, это должник — он покроет долг и доплатит при необходимости.

Пример 1:

Ввод: price = [-2,0,1,8,-9,0,1,2,3,0], k = 3
Вывод: [0,0,-72,0,0,0,6,0]
Объяснение: 0=-2*0*1, 0=0*1*8, -72=1*8*-9, ...
Пример 2:

Ввод: price = [-100,2], k = 1
Вывод: [-100,2]
Пример 3:

Ввод: price = [1,8,9], k = 5
Вывод: []
Ограничения:

len(price) ≥ 0
k ≥ 1
Значение массива price лежит в диапазоне [-10 000, 10 000] (включительно)
'''

# мое решение
def k_elements_multiply(price: list[int], k: int) -> list[int]:
    if len(price) < k:
        return []

    mult_list = []
    null_count = 0
    current_multiplication = 1
    for i in range(k):
        if price[i] == 0:
            null_count += 1
            continue
        current_multiplication = current_multiplication * price[i] if current_multiplication else price[i]
    if null_count:
        mult_list.append(0)
    else:
        mult_list.append(current_multiplication)

    l = 0
    r = k
    while r < len(price):
        if price[l] == 0:
            null_count -= 1
        else:
            current_multiplication = current_multiplication // price[l]
        if price[r] == 0:
            null_count += 1
        else:
            current_multiplication = current_multiplication * price[r]
        if null_count:
            mult_list.append(0)
        else:
            mult_list.append(current_multiplication)
        l += 1
        r += 1
    return mult_list


# эталонное решение
from typing import *


def k_elements_multiply(price: List[int], k: int) -> List[int]:
    if k > len(price):
        return []

    # число нулей в плавающем окне
    zero_count = 0
    # произведение всех элементов в плавающем окне за исключением нулевых
    non_zero_multiply = 1
    # заполняем окно
    for i in range(k):
        if price[i] == 0:
            zero_count += 1
            continue
        non_zero_multiply *= price[i]

    result: List[int] = [0]
    if zero_count == 0:
        result = [non_zero_multiply]

    # переходим от одного окна в другое
    for i in range(k, len(price)):
        # если элемент который выходит из окна == 0
        if price[i - k] == 0:
            zero_count -= 1
        else:
            non_zero_multiply //= price[i - k]

        # если элемент который приходит в окно == 0
        if price[i] == 0:
            zero_count += 1
        else:
            non_zero_multiply *= price[i]

        next_multiply = 0
        if zero_count == 0:
            next_multiply = non_zero_multiply
        result.append(next_multiply)
    return result


'''
Рост акций компании
средне
# решено

# яндекс
Дан массив stock, где stock[i] = 1 означает рост акций в i-й день, а stock[i] = -1 — падение. Требуется найти максимальное количество подряд идущих дней роста акций. 

Пример 1:

Ввод: stock = [-1,1,-1,1,1,1,1,-1,1]
Вывод: 4
Объяснение: Самый долгий рост акций - 4 дня (с 4 по 7 день).
Пример 2:

Ввод: stock = [1,-1,-1,1]
Вывод: 1
Ограничения:

0 <= len(stock)
Значение массива stock это -1 или 1
'''

# мое решение
def longest_stock_growth(nums: list[int]) -> int:
    current_count = 0
    max_count = 0
    for num in nums:
        if num == 1:
            current_count +=1
        else:
            current_count = 0
        max_count = max(max_count, current_count)
    return max_count


# эталонное решение 1
from typing import *

def longest_stock_growth(stock: List[int]) -> int:
    max_count = 0  # максимальное количество подряд идущих единиц
    count = 0  # текущее количество подряд идущих единиц
    for num in stock:
        if num == 1:
            count += 1
            # обновляем максимальное значение при необходимости
            max_count = max(max_count, count)
        else:
            count = 0  # сбрасываем счетчик, если встречается 0
    return max_count


# эталонное решение 2
from typing import *

def longest_stock_growth(stock: List[int]) -> int:
    l = 0
    r = 0
    result = 0
    while l < len(stock):
        while r + 1 < len(stock) and stock[r] == stock[r + 1]:
            r += 1

        if stock[r] == 1:
            result = max(result, r - l + 1)

        l = r + 1
        r = r + 1
    return result


'''
Сжатие значений счетчика
средне
# решено

# яндекс
Дан отсортированный по возрастанию массив уникальных чисел counter, где counter[i] — значение метрики в i-ю секунду.

Чтобы упростить восприятие, нужно сжать последовательность, объединяя подряд идущие числа например: [1,2,3,7] -> ["1->3","7"]:

Если числа идут подряд (разница = 1), записать в виде "x->y".
В остальных случаях оставить как есть ("x").
Пример 1:

Ввод: сounter = [1,2,3,4,5,8,10,15,16,20]
Вывод: ["1->5","8","10","15->16","20"]
Пример 2:

Ввод: сounter = [-3,-2]
Вывод: ["-3->-2"]
Пример 3:

Ввод: сounter = [0,2,4,6]
Вывод: ["0","2","4","6"]
Ограничения:

0 <= len(сounter)
'''

# мое решение (= эталонному, тк это задача из примера объяснения темы)
def counter_ranges(nums: list[int]) -> list[str]:
    l = 0
    r = 0
    result = []

    while r < len(nums):
        while r + 1 < len(nums) and nums[r] + 1 == nums[r + 1]:
            r += 1
        if r == l:
            result.append(str(nums[l]))
        else:
            result.append(f'{nums[l]}->{nums[r]}')
        l = r + 1
        r = r + 1

    return result


# эталонное решение
from typing import *

def counter_ranges(counter: List[int]) -> List[str]:
    l = 0
    r = 0
    result = []
    while l < len(counter):
        while r + 1 < len(counter) and counter[r] + 1 == counter[r + 1]:
            r += 1

        if r != l:
            result.append(f'{counter[l]}->{counter[r]}')
        else:
            result.append(f'{counter[l]}')

        l = r + 1
        r = r + 1
    return result


# best_parking_spot(nums = [1, 0, 0, 0, 1, 0, 1])
# best_parking_spot(nums = [1, 0, 0, 0])


'''
Лучшее место на парковке
средне
# решено

# яндекс
Дан массив spots, где spots[i] = 1 — занятое место, spots[i] = 0 — свободное. Нужно выбрать свободное место так, чтобы расстояние до ближайшей занятой машины было максимальным. Вернуть это максимальное расстояние.

Расстояние между местами — разность их индексов. Для каждого свободного места рассматривается ближайшая занятая машина слева и справа; берётся минимум из двух расстояний. Если с одной стороны машин нет — учитывается только другая сторона.

Важно: гарантировано есть хотя бы одно свободное и хотя бы одно занятое место.

Пример 1:


Ввод: spots = [0,1,0,0,0,1,0,1,0]
Вывод: 2
Объяснение: лучшее место — индекс 3. Слева ближайшая машина на индексе 1 (расстояние 2), справа — на индексе 5 (расстояние 2). Минимум = 2. Для всех остальных свободных мест минимальное расстояние меньше.
Пример 2:

Ввод: spots = [0,0,0,1,0,1]
Вывод: 3
Объяснение: лучшее место — индекс 0. Машин слева нет, справа ближайшая на индексе 3 (расстояние 3).
Пример 3:

Ввод: spots = [1,0,0,1]
Вывод: 1
Ограничения:

len(spots) >= 2
Значение каждого элемента: 0 или 1
'''

# мое решение
def best_parking_spot(nums: list[int]) -> int:
    # 1. найти индексы самого большого окна среди нулей
    # 2. найти среднее между правым и левым индексом

    l = 0
    r = 0
    max_distance = 1
    while r < len(nums):
        while r + 1 < len(nums) and nums[r] == nums[r + 1]:
            r += 1
        if nums[r] == 0:
            if l == 0:
                max_distance = max(max_distance, r + 1 - l)
            elif r == len(nums) - 1:
                max_distance = max(max_distance, r - l + 1)
            else:
                window_size = r - l + 1
                place = (r + l) // 2
                max_distance = max(max_distance, min(place - l + 1, r + 1 - place))
        l = r + 1
        r = r + 1

    return max_distance


# эталонное решение
from typing import *

def best_parking_spot(spots: List[int]) -> int:
    l = 0
    r = 0
    result = 0
    while l < len(spots):
        while r + 1 < len(spots) and spots[r] == spots[r + 1]:
            r += 1

        # обновляем ответ, только если в плавающем окне были нули
        if spots[r] == 0:
            # если 0 прижат к стенке слева или справа,
            # то свободных мест будет r - l + 1, т. к. посадим в самый край
            if l == 0 or r == len(spots) - 1:
                result = max(result, r - l + 1)
            # окно располагается между 1-ами:
            # поэтому находим число мест по формуле (r - l + 2) // 2
            else:
                result = max(result, (r - l + 2) // 2)

        l = r + 1
        r = r + 1
    return result

'''
Кодирование повторов
средне
# решено

# озон

# яндекс
Дан массив chars и нужно реализовать алгоритм сжатия строки по следующим правилам:

Подряд идущие одинаковые символы группируются.
Группа включает в себя всегда максимально возможное число одинаковых подряд идущих символов.
Если в группе только одна буква, то пишется только она.
Если в группе более одной буквы, то пишется сначала буква, а потом число раз, которое она встретилась.
Если буква встретилась более 9 раз, то каждый символ количества должен быть записан отдельно.
Пример 1:

Ввод: chars = ["x","x","y","z","z","z"]
Вывод: ["x","2","y","z","3"]
Пример 2:

Ввод: chars = ["y","y","x","x","x","x","x","x","x","x","x","x","x","x","y","y"]
Вывод: ["y","2","x","1","2","y","2"]
Пример 3:

Ввод: chars = ["a","b","c"]
Вывод: ["a","b","c"]
Ограничения:

0 <= len(chars)
Массив chars может содержать только английские буквы.
'''

# мое решение
def compress(chars: list[str]) -> list[str]:
    result = []
    l = 0
    r = 0
    while r < len(chars):
        while r+1 < len(chars) and chars[r] == chars[r+1]:
            r+=1
        if l == r:
            result.append(chars[l])
        else:
            result.append(chars[l])
            count = r - l + 1
            if count < 10:
                result.append(str(count))
            else:
                for c in str(count):
                    result.append(c)
        l = r+1
        r = r+1
    return result


# эталонное решение
def compress(chars: List[str]) -> List[str]:
    l = 0
    r = 0
    result = []
    while l < len(chars):
        # бежим правым указателем, пока в интервале [l, r]
        # находятся все одинаковые символы
        while r + 1 < len(chars) and chars[r] == chars[r + 1]:
            r += 1

        # обновляем ответ
        windowSize = r - l + 1
        if windowSize == 1:
            result.append(chars[r])
        else:
            result.append(chars[r])
            result += list(str(windowSize))

        # интервалы не пересекаются, поэтому сдвигаем
        # на r + 1 - именно отсюда будет начинаться
        # следующий интервал
        l = r + 1
        r = r + 1
    return result


# Паттерн "Пересекающиеся окна"
from typing import *

#
# def calculate(nums: List[int]) -> List[str]:
#     l = 0
#     # обрати внимание, что r = -1
#     r = -1
#     # Здесь можно добавить другие переменные, если они используются в вашем коде
#     while l < len(nums):
#         while r + 1 < len(counter) and  # тут условие, что следующий элемент можно взять в окно
#             # возможна дополнительная обработка ...
#             r += 1
#
#         # обновляем ответ
#         # ...
#
#         # обновляем состояние плавающего окна перед сдвигом
#         # ...
#
#         # сдвигаем левый указатель
#         l += 1
#     return result


'''
Цепочка из k-генов
средне
# решено

# желтый банк
Дана строка gene, представляющая последовательность генов, где каждый ген — это один символ.

Требуется найти самую длинную непрерывную подстроку, содержащую не более k уникальных генов, где k ≤ числа различных символов.

Пример 1:

Ввод: gene = "YYxxXXXyyy", k = 3
Вывод: 8
Объяснение: самая длинная непрерывная последовательность генов с максимум 3-мя разными генами это "xxXXXyyy" (регистр буквы имеет значение).
Пример 2:

Ввод: gene = "yyy", k = 0
Вывод: 0
Пример 3:

Ввод: gene = "aXYYYXYXYbccc", k = 1
Вывод: 3
Ограничения:

0 <= len(gene)
0 <= k <= len(gene)
gene содержит ASCII символы
'''

# мое решение
from collections import defaultdict
def longest_gene_sequence(nums: str, target: int) -> int:
    r = -1
    l = 0
    result = 0

    if target == 0:
        return result
    counter = defaultdict(int)
    while l < len(nums):
        while r + 1 < (len(nums)) and (len(counter) < target or nums[r + 1] in counter):
            counter[nums[r + 1]] += 1
            r += 1

        result = max(result, r - l + 1)
        counter[nums[l]] -= 1
        if counter[nums[l]] == 0:
            del counter[nums[l]]
        l += 1

    return result


# эталонное решение
from typing import *

def longest_gene_sequence(gene: str, k: int) -> int:
    l = 0
    # r = -1, чтобы добавление первого элемента не было исключением
    r = -1
    result = 0

    # ключ: название гена, значение: сколько раз встретился ген в плавающем окне
    gene_count: dict[str, int] = {}

    while l < len(gene):
        while r + 1 < len(gene) and (len(gene_count) < k or gene[r + 1] in gene_count):
            gene_count[gene[r + 1]] = gene_count.get(gene[r + 1], 0) + 1
            r += 1

        # обновляем ответ
        window_size = r - l + 1
        result = max(result, window_size)

        # двигаем l (левую границу окна) на 1 и обновляем число уникальных символов
        gene_count[gene[l]] = gene_count.get(gene[l], 0) - 1
        if gene_count[gene[l]] <= 0:
            # <=, а не == т.к. при k = 0 gene_count[gene[l]] -= 1 добавит ключ gene[l]
            # а так происходить не должно, поэтому условие <= 0
            del gene_count[gene[l]]
        l += 1

    return result
