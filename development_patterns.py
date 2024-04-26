# MVC

class Model:
    def __init__(self):
        self.data = []

    def add_data(self, new_data):
        self.data.append(new_data)


class View:
    def show_data(self, data):
        print(f"{data=}")


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def add_data(self, new_data):
        self.model.add_data(new_data)
        self.view.show_data(self.model.data)


controller = Controller()
controller.add_data("hello")
controller.add_data("world")

'''
Model
Модель представляет собой компонент приложения, который отвечает за хранение данных и логику их обработки.
Она не зависит от других компонентов и может использоваться в различных контекстах.
Модель может быть представлена в виде классов, структур или баз данных.

View
Представление - это компонент, который отвечает за отображение данных пользователю.
Она не содержит логики и не взаимодействует напрямую с моделью.
Представление может быть представлено в виде графического интерфейса, 
веб-страницы или другого типа пользовательского интерфейса.

Controller
Контроллер - это компонент, который управляет взаимодействием между моделью и представлением.
Он получает запросы от пользователя через представление, обрабатывает их с помощью модели и возвращает результат
обратно в представление. Контроллер может изменять состояние модели и обновлять представление в соответствии с этим 
состоянием.
'''

# Factory method

'''
Фабричный метод (Factory Method) - это порождающий паттерн проектирования, который позволяет создавать объекты без 
указания их конкретных классов. 
Вместо этого он предоставляет интерфейс для создания объектов в суперклассе, 
который может быть переопределен в подклассах для изменения типа создаваемого объекта.
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!!"


class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == 'Dog':
            return Dog()
        if animal_type == 'Cat':
            return Cat()
        else:
            return None


factory = AnimalFactory()

animal = factory.create_animal("Dog")
print(animal.speak())

animal = factory.create_animal("Cat")
print(animal.speak())


# Singleton

"""
Singleton - паттерн проектирования "Одиночка".
Одиночка (Singleton) — это паттерн проектирования, который обеспечивает создание одного и только одного экземпляра
класса, и предоставляет глобальную точку доступа к этому экземпляру.


Для реализации Одиночки необходимо скрыть конструктор класса и предоставить статический метод,
который будет создавать (если он ещё не был создан) и возвращать единственный экземпляр класса.

Классический пример использования паттерна Одиночка - это логгеры. Каждый раз, когда приложение пишет лог,
необходимо получать доступ к единственному экземпляру логгера.

- Конфигурационные настройки. Класс с настройками приложения. Singleton обеспечит одну точку доступа к настройкам
и весь код сможет ссылаться на одни и те же настройки

- Подключение к базе данных -- Singleton гарантированно создаст только один экземпляр класса, отвечающий за подключение
к ней

- Счетчики и глобальные объекты.

-Пул ресурсов. Если у нас ограниченный пул соединений к внешнему сервису или к другим ресурсам, 
то Singleton гарантирует, что доступ к ним всегда будет идти через единственный экземпляр.
"""


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init(self):
        pass


'''
Проблемы Singleton:
    - Глобальное состояние. Singleton доступен из любой части программы, то есть сломать его может кто угодно.
    - Потокобезопасность. Разные потоки могут наштамповать кучу синглтонов. Нужно предусмотреть механизмы синхронизации
    - Тестированиею. Для тестирования класса с Singleton потребуются мок-обекты.
'''


# Strategy
'''
Паттерн проектирования Стратегия. Поведенческий паттерн проектирования. Его задача - выделить схожие алгоритмы,
решающие конкретную задачу. Реализация алгоритмов выносится в отдельные классы и предоставляется возможность
выбирать алгоритмы во время выполнения программы.

Основные участники паттерна:
    - Контекст - объект, который содержит ссылку на объект конкретной стратегии
    - Стратегия - интерфейс, который определяет операции, которые должны быть реализованы в каждом алгоритме
    - Конкретная стратегия - класс, который реализует интерфейс стратегии и содержит конкретный алгоритм
    
Например, задача по сортировке массива:
'''

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSort(Strategy):
    def sort(self, data):
        print("Sorting using Bubble sort")
        return data


class QuickSort(Strategy):
    def sort(self, data):
        if len(data) < 2:
            return data
        pivot = data[0]
        less = [item for item in data[1:] if item <= pivot]
        greater = [item for item in data[1:] if item > pivot]
        return self.sort(less) + [pivot] + self.sort(greater)


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)


data = [5, 2, 1, 4, 10, 6]
context = Context(BubbleSort())
sorted_data = context.sort(data)
print(sorted_data)

context.set_strategy(QuickSort())
sorted_data = context.sort(data)
print(sorted_data)


# Facade

'''
Паттерн Фасад - структурный паттерн проектирования, который позволяет скрыть сложность и множество интефейсов
системы путем предоставления простого объединенного интерфейса. 
Фасад не дает никакой информации об устройстве здания за ней. Так же фасад программного приложения скрывает 
внутреннюю сложность системы и предоставляет упрощенный интерфейс для доступа к ее функционалу.
'''

class Facade:
    def __init__(self, subsystem1=None, subsystem2=None):
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self):
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation2())
        results.append("Facade orders subsystems to perform the action")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


# Подсистемы
class Subsystem1:
    def operation1(self):
        return "Subsystem1: Ready!"

    def operation_n(self):
        return "Subsystem1: Go!"


class Subsystem2:
    def operation2(self):
        return "Subsystem2: Get set!"

    def operation_z(self):
        return "Subsystem2: Fire!"


# Клиентский код
def client_code(facade: Facade) -> None:
    print(facade.operation())

# Создаем подсистемы
subsystem1 = Subsystem1()
subsystem2 = Subsystem2()

# Создаем фасад и передаем ему подсистемы
facade = Facade(subsystem1, subsystem2)

# Запускаем клиентский код
client_code(facade)
