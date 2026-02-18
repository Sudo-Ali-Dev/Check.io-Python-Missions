# https://py.checkio.org/en/mission/count-divisibles-in-range-simplified/

def count_divisible(n: int, k: int) -> int:
    # return int(n / k) --> Normal division results in float and then convert it into int.
    return n // k # floor division automatically round to nearest number and results in int

print("Example:")
print(count_divisible(2, 1))

# These "asserts" are used for self-checking
assert count_divisible(10, 2) == 5
assert count_divisible(10, 3) == 3
assert count_divisible(10, 5) == 2
assert count_divisible(15, 4) == 3
assert count_divisible(20, 6) == 3
assert count_divisible(100, 10) == 10
assert count_divisible(200, 25) == 8
assert count_divisible(50, 7) == 7
assert count_divisible(60, 8) == 7
assert count_divisible(70, 9) == 7

print("The mission is done! Click 'Check Solution' to earn rewards!")
