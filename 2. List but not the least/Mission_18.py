# https://py.checkio.org/en/mission/sort-except-zero/ 
# Simple

from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    
    items_len = len(items)

    zero_place = []
    i = items_len - 1
    while i >= 0:
        if items[i] == 0:
            zero_place.append(i)
            items.pop(i)
        i -= 1

    sorted = []

    j = 0
    while j < items_len:
        if j in zero_place:
            sorted.append(0)
            j += 1 
            continue
        min_digit = min(items)
        sorted.append(min_digit)
        items.pop((items.index(min_digit)))

        j += 1 
    
    return sorted

print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

# These "asserts" are used for self-checking
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
