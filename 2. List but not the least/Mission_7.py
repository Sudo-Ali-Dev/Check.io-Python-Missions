# https://py.checkio.org/en/mission/replace-first/

from collections.abc import Iterable

def replace_first(items: list) -> Iterable:
    if len(items) == 0:
        return []
    else:
        return (items[1::]) + [items[0]]


# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
