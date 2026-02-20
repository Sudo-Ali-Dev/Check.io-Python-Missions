# https://py.checkio.org/en/mission/number-length/

def number_length(value: int) -> int:
    sum = 0
    for digit in str(value):
        sum = sum + 1
    return sum


print("Example:")
print(number_length(10))

# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")
