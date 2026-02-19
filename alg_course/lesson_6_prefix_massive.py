
'''
Условие
Реализуй структуру данных, которая позволяет быстро находить
сумму всех элементов на отрезке [l, r] (включая границы). При этом массив не изменяется.

Другими словами, нужно реализовать:

Конструктор (вызывается один раз).
Метод sum (вызывается многократно, поэтому он должен быть максимально быстрым).
'''
from collections import defaultdict
from typing import *

class PrefixArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            # создаем префиксный массив
            # общую сумму складываем с num и таким образом у нас всегда есть сумма на каждом элементе
            self.prefix.append(self.prefix[-1] + num)  # так мы создаем префиксный массив


    def sum(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


# мое решение
def count_subarrays(nums: List[int], target_sum: int) -> int:
    common_count = 0
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    hash_map = defaultdict(int)
    for num in prefix:
        if num in hash_map:
            common_count += hash_map[num]
        hash_map[num + target_sum] +=1
    return common_count

# nums = [1, 1, 1]
# target = 2
#
# count_subarrays(nums, target)


def max_queen_sum(board: List[List[int]]) -> int:
    rows_sum = [0] * len(board)
    col_sum = [0] * len(board[0])
    d1_sum = [0] * (len(board) + len(board[0]) - 1)
    d2_sum = [0] * (len(board) + len(board[0]) - 1)

    for i in range(len(board)):
        for j in range(len(board[i])):
            val = board[i][j]
            rows_sum[i] += val
            col_sum[j] += val
            d1_idx = j-i+len(board) - 1
            d1_sum[d1_idx] += val
            d2_sum[i+j] += val

    max_sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            row = rows_sum[i]
            col = col_sum[j]
            d1 = d1_sum[j-i+len(board) - 1]
            d2 = d2_sum[j+i]
            current_sum = row+col+d1+d2 - (board[i][j]*3)
            if i == 0 and j == 0:
                max_sum = current_sum
            max_sum = max(max_sum, current_sum)
    return max_sum

