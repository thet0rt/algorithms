'''
Задача 1. Про массив и сумму чисел
У нас есть массив с целыми числами, как с положительными, так и отрицательными. Все числа в массиве разные.
Если сложить или вычесть любые два числа из массива, они точно поместятся в стандартной целочисленной переменной.

Ещё у нас есть какое-то целое число — оно не в массиве, а само по себе, отдельной переменной.

Решение заключается в том, чтобы идти по списку и записывать разность между target и элементом массива. В ключи кладем
разницу, а в значение его индекс. На каждой итерации проверяем, если эта разница уже есть в словаре, то просто берем
индекс этого элемента
'''

nums = [2, 4, 5, 1, 8]

target = 5

def two_sum(nums, target):
    answer = 'В массиве нет такой пары чисел'
    hash_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map:
            answer = 'Ответ: ' + str(hash_map[complement])
        hash_map[nums[i]] = i
    return answer


'''
Задача 2. Как найти палиндром
Идея в том, чтобы переворачивать число! 
Отсекаем по одному числу с конца и записываем его в новое число. Делаем это пока не дойдем до середины числа
'''
def palindrome(x: int) -> bool:
    if not x:
        return False
    elif x < 0:
        return False
    elif not x % 10:
        return False
    temp = 0
    preX = x

    while x > temp:  # пока не дойдем до середины числа
        pop = x % 10
        preX = x
        x = x // 10
        temp = temp*10 + pop
    if x == temp or preX == temp:
        return True
    else:
        return False


'''
Задача 3. Найти самую длинную вложенную строку.
Найти длину самой длинной подстроки, в которой каждый символ используется только один раз.
Можно перебрать начиная с каждого индекса, записывая в список, какие буквы встречаются.

Суть в том, что мы перебираем элементы, если элем встречается в подстроке, то мы передвигаем подстроку на 1 элемент
'''

def find_str(initial:str) -> int:
    res = 0
    sub = ''
    for char in initial:
        if char not in sub:
            sub += char
            res = max(res, len(sub))
        else:
            ind = sub.index(char)
            sub = sub[ind+1:] + char



'''
Задача 4. Про перебор букв в словах.
Есть массив со словами, в котором есть хотя бы одно слово. Надо найти максимально длинное общее начало каждого слова.
Если такого нет — вывести пустую строку.
'''

a = ['дом', 'домен', 'домра', 'доширак']
max_length = 0
max_word = ''
for item in a:
    item_length = len(item)
    if item_length > max_length:
        max_length = item_length
        max_word = item

max_common_str = ''
for i in range(1, len(max_word)):
    if not all([item.startswith(max_word[:i]) for item in a]):
        break
    max_common_str = max_word[:i]
print(max_common_str)



"""
Задача 5. Код берет строку с запросом, проверяет и сообщает, в порядке там скобки или нет.
Решение: нам надо выписать все скобочки в отдельную строку. И в ней уже проверять и удалять парные () {} []
"""


def find_brackets(input: str) -> bool:
    brackets = '{}()[]'
    new_str = ''
    for x in input:
        if x in brackets:
            new_str += x
    while ('{}' in new_str) or ('[]' in new_str) or '()' in new_str:
        new_str = new_str.replace('{}', '').replace('[]', '').replace('()', '')

    if new_str:
        return False
    return True



'''
Задача 6.
'''