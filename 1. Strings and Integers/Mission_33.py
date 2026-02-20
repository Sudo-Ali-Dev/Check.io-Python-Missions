# https://py.checkio.org/en/mission/reverse-integer/

def reverse_digits(num: int) -> int:
    int_string = str(num)
    start_with = int_string.startswith("-")
    if start_with:
        newString = int_string[0] + int_string[1:][::-1]
        return int(newString)
    else:
        return int(int_string[::-1])


print("Example:")
print(reverse_digits(-123))

# These "asserts" are used for self-checking
assert reverse_digits(1234) == 4321
assert reverse_digits(0) == 0
assert reverse_digits(-123) == -321
assert reverse_digits(5) == 5
assert reverse_digits(-9) == -9
assert reverse_digits(100) == 1
assert reverse_digits(-100) == -1
assert reverse_digits(54321) == 12345
assert reverse_digits(1111) == 1111
assert reverse_digits(987654321) == 123456789

print("The mission is done! Click 'Check Solution' to earn rewards!")
