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
