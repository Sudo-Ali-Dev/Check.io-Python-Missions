# https://py.checkio.org/en/mission/majority/

def is_majority(items: list[bool]) -> bool:

    true_times = 0
    false_times = 0

    for x in items:
        if x is True:
            true_times += 1
        else:
            false_times += 1

    if true_times > false_times:
        return True
    else:
        return False

print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
