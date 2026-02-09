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
