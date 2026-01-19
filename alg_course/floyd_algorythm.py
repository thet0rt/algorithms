'''
Алгоритм Флойда позволяет найти цикл в связном списке и найти начало цикла.
'''


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

a = ListNode(3)
b = ListNode(5)
a.next = b
c = 1
b.next = c

def insert_after(node, value):
    new_node = ListNode(value)
    new_node.next = node.next
    node.next = new_node

insert_after(a, 7)

[3, 5, 1]


# создаем связный список с циклом
def create_list_with_cycle(num: int):
    nodes = [ListNode(i) for i in range(1, num)]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    nodes[-1].next = nodes[2]  # цикл начинается в узле со значением 3

    return nodes[0]

# Сам алгоритм.
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# функция с трейсом в консоли
def trace_cycle_detection(head):
    slow = head
    fast = head
    step = 0

    print("=== Поиск точки встречи ===")

    while fast and fast.next:
        step += 1
        slow = slow.next
        fast = fast.next.next

        print(
            f"Шаг {step}: "
            f"slow -> {slow.value}, "
            f"fast -> {fast.value}"
        )

        if slow == fast:
            print(f"\n🎯 Встреча произошла в узле {slow.value}\n")
            return slow

    print("\n❌ Цикла нет\n")
    return None

trace_cycle_detection(create_list_with_cycle(20))


def trace_cycle_start(head, meeting_node):
    slow = head
    fast = meeting_node
    step = 0

    print("=== Поиск начала цикла ===")

    while slow != fast:
        step += 1
        slow = slow.next
        fast = fast.next

        print(
            f"Шаг {step}: "
            f"slow -> {slow.value}, "
            f"fast -> {fast.value}"
        )

    print(f"\n🎯 Начало цикла найдено в узле {slow.value}\n")
    return slow

trace_cycle_start(create_list_with_cycle(20), 18)


