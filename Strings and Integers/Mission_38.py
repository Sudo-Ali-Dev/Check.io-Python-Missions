# https://py.checkio.org/en/mission/end-zeros/

def end_zeros(a: int) -> int:

    reverse_a = str(a)[::-1]
    
    num_of_zeros = 0
    
    for digit in reverse_a:
        if digit.startswith("0"):
            num_of_zeros = num_of_zeros + 1
        else:
            break
    
    return num_of_zeros


print("Example:")
print(end_zeros(101))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")