# https://py.checkio.org/en/mission/beginning-zeros/

def beginning_zeros(a: str) -> int:
    
    timesZero = 0
    for digit in str(a):
        if digit == "0":
            timesZero += 1
        else:
            break
    
    return timesZero

print("Example:")
print(beginning_zeros("0000"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
