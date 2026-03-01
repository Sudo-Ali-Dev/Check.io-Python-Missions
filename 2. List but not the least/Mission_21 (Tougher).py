# https://py.checkio.org/en/mission/changing-direction/
# Simple

def changing_direction(elements: list[int]) -> int:
    directions = []

    for i, j in zip(elements, elements[1:]):
        if j > i and (not directions or directions[-1] == '-'):
            directions.append('+')
        elif j < i and (not directions or directions[-1] == '+'):
            directions.append('-')

    return (len(directions)) - bool(directions)

print("Example:")
print(changing_direction([5, 4, 1]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
