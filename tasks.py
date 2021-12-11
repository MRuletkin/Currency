# task 1

def split_list(numbers: list, divisor: int) -> list:
    new_list = []
    for i in range(0, len(numbers), divisor):
        new_list.append(numbers[i: i + divisor])
    return new_list


assert split_list([1, 2, 3, 4], 2) == [
    [1, 2],
    [3, 4],
]
assert split_list([1, 2, 3, 4, 5, 6], 2) == [
    [1, 2],
    [3, 4],
    [5, 6],
]
assert split_list([1, 2, 3, 4, 5, 6], 3) == [
    [1, 2, 3],
    [4, 5, 6],
]
assert split_list([1, 2, 3, 4, 5], 3) == [
    [1, 2, 3],
    [4, 5],
]
assert split_list([1, 2, 3, 4, 5], 2) == [
    [1, 2],
    [3, 4],
    [5, ],
]
assert split_list([1, 2, 3, 4, 5], 10) == [
    [1, 2, 3, 4, 5],
]
assert split_list([], 2) == [
]
