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

