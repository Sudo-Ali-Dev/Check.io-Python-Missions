# https://py.checkio.org/en/mission/median/

def checkio(data: list[int]) -> int | float:
    list_length = len(data)
    sorted_list = []
    i = 0
    while i < list_length:
        min_digit = min(data)
        sorted_list.append(min_digit)
        data.remove(min_digit)
        i += 1

    if list_length % 2 == 0:
        result = list_length // 2
        return float(((sorted_list[(result - 1)] + sorted_list[result])) / 2)
    else:
        result = list_length // 2
        return sorted_list[(result)]


print("Example:")
print(checkio([3, 6, 20, 99, 10, 15]))

# These "asserts" are used for self-checking
assert checkio([1, 2, 3, 4, 5]) == 3
assert checkio([3, 1, 2, 5, 3]) == 3
assert checkio([1, 300, 2, 200, 1]) == 2
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
assert checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
assert checkio([33, 56, 62]) == 56
assert checkio([21, 56, 84, 82, 52, 9]) == 54
assert checkio([100, 1, 1, 1, 1, 1, 1]) == 1
assert checkio([64, 6, 92, 7, 70, 5]) == 35.5

print("The mission is done! Click 'Check Solution' to earn rewards!")