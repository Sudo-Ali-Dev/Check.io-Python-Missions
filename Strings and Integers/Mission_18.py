# https://py.checkio.org/en/mission/number-with-exclamation/

def factorial(n: int) -> int:

# Loop Method

    # result = 1
    # for i in range (1, n + 1):
    #     result = result * i
    # return result

# Recursion Method

    return n * factorial(n - 1) if n > 1 else 1

print("Example:")
print(factorial(4))

# These "asserts" are used for self-checking
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
assert factorial(15) == 1307674368000

print("The mission is done! Click 'Check Solution' to earn rewards!")
