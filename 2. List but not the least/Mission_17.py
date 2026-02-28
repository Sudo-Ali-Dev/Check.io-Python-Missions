# https://py.checkio.org/en/mission/non-unique-elements/
# Elementary+

from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:

    ind = len(data) - 1
    while ind >= 0:
        count = 0
        for digit in data:
            if digit == data[ind]:
                count += 1
        if count == 1:
            data.pop(ind)
        ind -= 1
        
    return data


print("Example:")
print(list(checkio([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
assert list(checkio([1, 2, 3, 4, 5])) == []
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
assert list(checkio([10, 20, 30, 10])) == [10, 10]
assert list(checkio([7])) == []
assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
assert list(checkio([99, 98, 99])) == [99, 99]
assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
