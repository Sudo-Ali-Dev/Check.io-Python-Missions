# https://py.checkio.org/en/mission/even-last/

def checkio(array: list[int]) -> int:

    if len(array) == 0:
        return 0

    new_list = []
    
    i = 0
    while i < len(array):
        new_list.append(array[i])
        i += 2

    final_digit = array[-1]    

    result = sum(new_list) * final_digit

    return result

print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
