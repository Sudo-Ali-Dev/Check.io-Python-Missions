# https://py.checkio.org/en/mission/changing-direction/
# Simple

def changing_direction(elements: list[int]) -> int:
    count = 0
    i = 1
    while i < len(elements) - 1:
        if elements[i - 1] > elements[(i)] and elements[(i)] < elements[(i + 1)]:
            count += 1
        i += 1

print("Example:")
print(changing_direction([1, 2, 2, 1, 2, 2]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
