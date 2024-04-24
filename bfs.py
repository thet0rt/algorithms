"""
Поиск в ширину. Применяется к графам. Графы в программировании реализуются посредством словарей.
Например:
"""
graph = {}
graph['me'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['claire']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

"""
Граф выше является направленным. Мы видим, что alice -> claire, но claire !-> alice
"""

"""
Реализация bash команды tail с помощью двусторонней очереди deque
"""


def tail(filename, n):
    from collections import deque
    with open(filename, 'r') as file:
        return deque(file, n)


print(tail('file.txt', 10))


def breadth_first_search():
    from collections import deque
    search_queue = deque()
    search_queue += graph['you']
    searched = []

    def person_is_seller(name):
        return name[-1] == 'm'

    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + ' is a mango seller')
        else:
            search_queue += graph[person]
            searched.append(person)
    return False


breadth_first_search()



"""
Алгоритм Дейкстры. Используется для поиска пути с наименьшим весом в направленных ациклических графах без отрицательных
ребер.
"""



graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 3
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}
print(graph)

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
print(costs)

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
print(parents)

processed = []


def find_lowest_cost_node(costs: {}):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # перебираем все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # если это узел с наименьшей стоимостью и еще не был обработан
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_code_node(costs)  # найти узел с наименьшей стоимостью среди необработанных
while node is not None:  # если обработаны все узлы, цикл while завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # если к соседу добраться можно через текущий узел
            costs[n] = new_cost  # то обновляем стоимость для этого узла
            parents[n] = node  # этот узел становится новым родителем для соседа
    processed.append(node)  # узел помечается как обработанный
    node = find_lowest_code_node(costs)  # найти следующий узел для обработки и повтороить цикл
