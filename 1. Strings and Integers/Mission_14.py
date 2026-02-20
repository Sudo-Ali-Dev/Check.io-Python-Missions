# https://py.checkio.org/en/mission/fizz-buzz/

# Taken from mission Just Fizz!
# https://py.checkio.org/en/mission/just-fizz/
def checkio(num: int) -> str:
    
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else: 
        return str(num)


print("Example:")
print(checkio(15))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")
