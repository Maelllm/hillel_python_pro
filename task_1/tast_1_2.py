import functools
import tracemalloc


def size(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start = tracemalloc.get_tracemalloc_memory()
        function(*args, **kwargs)
        return f'You used {tracemalloc.get_tracemalloc_memory() - start} bytes' \
               f' to evaluate {function.__name__} result {function(*args, **kwargs)}'

    return wrapper


# Just for displaying results
@size
def foo(num_1, num_2, num_3):
    num_1 = num_1 ** 45
    num_2 = num_2 ** 54
    num_3 = sum(range(num_3, 40000))
    return (num_1 - num_2) / num_3


@size
def foo_2(num_1, num_2, num_3, num_4):
    num_1 = num_1 ** num_2
    num_3 = num_3 ** num_4
    return num_1 - num_3


print(foo(44, 5, 3))
print(foo_2(44, 5, 3, 43))
