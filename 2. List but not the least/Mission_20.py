# https://py.checkio.org/en/mission/absolute-sorting/
# Elementary

def checkio(values: list) -> list:
    
    # return sorted(values, key=abs) # Ironically, I could have solved the mission using this line only

    new_values = []
    ref_values = []
    for digit in values:
        if digit < 0:
            ref_values.append(abs(digit))
            new_values.append(abs(digit))
        else:
            new_values.append(digit)
    sorted_values = sorted(new_values)

    i = 0
    while i < len(ref_values):
        if ref_values[i] in sorted_values:
            ref_ind = sorted_values.index(ref_values[i])
            sorted_values[ref_ind] *= -1
        i += 1

    return sorted_values

print("Example:")
print(checkio([-20, -5, 10, 15]))

# These "asserts" are used for self-checking
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]

print("The mission is done! Click 'Check Solution' to earn rewards!")
