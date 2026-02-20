# https://py.checkio.org/en/mission/armstrong-number-checking/

def is_armstrong(num: int) -> bool:
    
    num_string = str(num)
    power_result = []

    for digit in num_string:
        i = 1
        int_digit = int(digit)
        power = int_digit
        while i < len(num_string):
            int_digit = int_digit * power
            i = i + 1
        power_result.append(int_digit)

    sum_power = sum(power_result)

    if sum_power == num:
        return True
    else:
        return False

print("Example:")
print(is_armstrong(370))

# These "asserts" are used for self-checking
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True
assert is_armstrong(407) == True
assert is_armstrong(163) == False
assert is_armstrong(100) == False
assert is_armstrong(8208) == True
assert is_armstrong(930) == False
assert is_armstrong(4) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
