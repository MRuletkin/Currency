# task 1
import requests


# def split_list(numbers: list, divisor: int) -> list:
#     new_list = []
#     for i in range(0, len(numbers), divisor):
#         new_list.append(numbers[i: i + divisor])
#     return new_list
#
#
# assert split_list([1, 2, 3, 4], 2) == [
#     [1, 2],
#     [3, 4],
# ]
# assert split_list([1, 2, 3, 4, 5, 6], 2) == [
#     [1, 2],
#     [3, 4],
#     [5, 6],
# ]
# assert split_list([1, 2, 3, 4, 5, 6], 3) == [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
# assert split_list([1, 2, 3, 4, 5], 3) == [
#     [1, 2, 3],
#     [4, 5],
# ]
# assert split_list([1, 2, 3, 4, 5], 2) == [
#     [1, 2],
#     [3, 4],
#     [5, ],
# ]
# assert split_list([1, 2, 3, 4, 5], 10) == [
#     [1, 2, 3, 4, 5],
# ]
# assert split_list([], 2) == [
# ]

def lru_cache(function):
    CACHE = {}

    def wrapper(*args, **kwargs):
        key = f'{function.__name__}::{args}-{kwargs}'
        print(CACHE)
        if key in CACHE:
            return CACHE[key]
        from time import sleep
        sleep(2)
        result = function(*args, **kwargs)
        CACHE[key] = result
        return result

    return wrapper


@lru_cache
def add(x, y):
    return x + y


@lru_cache
def foo():
    return 1


print(add(2, 5))
print(add(2, 5))
# print(add(2, y=5))
# print(add(3, 4))
# print(add(3, 5))
# print(foo())
# print(add(3, 4))
