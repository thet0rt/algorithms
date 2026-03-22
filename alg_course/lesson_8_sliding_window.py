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