# Selection sort algorithm

def find_smallest(data: list) -> int:
    smallest = data[0]  # здесь храним наименьшее значение
    smallest_index = 0  # здесь храним индекс наименьшего значения
    for i in range(1, len(data)):
        if data[i] < smallest:  # сравниваем наименьшее значение со всеми элементами списка
            smallest = data[i]
            smallest_index = i
    return smallest_index


def selection_sort(data: list) -> list:
    list_sorted = []
    for i in range(len(data)):
        smallest = find_smallest(data)
        list_sorted.append(data.pop(smallest))
    return list_sorted


def bubble_sort(data: list) -> list:
    '''
    Метод сортировки массивов и списков путем последовательного сравнения соседних элементов и их обмена,
    если предшествующий оказывается больше предыдущего
    Количество итераций внешнего цикла = Длина списка - 1
    Количество итераций внутреннего цикла зависит от номера итерации внешнего цикла
    :param data:
    :return:
    '''
    N = len(data)
    for i in range(N-1):
        for j in range(N-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def selection_sort(data: list) -> list:

    def find_smallest(data: list) -> int:
        smallest = data[0]
        smallest_ind = 0
        for i, item in enumerate(data[1:], 1):
            if item < smallest:
                smallest = item
                smallest_ind = i
        return smallest_ind

    list_sorted = []
    while data:
        list_sorted.append(data.pop(find_smallest(data)))


