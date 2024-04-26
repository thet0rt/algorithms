# Декораторы и генераторы

'''
Главное понять логику декоратора.
Декоратор должен возвращать функцию, перед или после которой выполняется определенный код
'''


def test_dec(func):
    return func


@test_dec
def double(a: int) -> int:
    print(a*2)
    return a*2


def working_decorator(func):
    def wrapper():
        print('до результата')
        result = func()
        print('после результата')
        return result
    return wrapper


@working_decorator
def triple() -> int:
    print(3*3)
    return 3*3

triple()


def dec_with_args(func):
    def wrapper(*args, **kwargs):
        print('до результата')
        result = func(*args, **kwargs)
        print('после результата')
        return result
    return wrapper


@dec_with_args
def double_2(a: int) -> int:
    print(a*2)
    return a*2


double_2(6)


def dec_using_arg_kwarg(*args, **kwargs):
    def actual_decorator(func):
        def wrapper(*args2, **kwargs2):
            print(f'до результата {args}')
            result = func(*args2, **kwargs2)
            print(f'после результата {kwargs}')
            return result
        return wrapper
    return actual_decorator


@dec_using_arg_kwarg(5, 3, 4, a=1, b=2, c=3)
def double_3(a: int) -> int:
    print(a*2)
    return a*2


double_3(12)



def func1(a: int):
    for i in range(a):
        yield i ** 2
    print('конец')
    return 1

a = func1(4)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
