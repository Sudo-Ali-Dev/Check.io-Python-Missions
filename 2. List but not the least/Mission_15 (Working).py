# https://py.checkio.org/en/mission/non-empty-lines/

def non_empty_lines(text: str) -> int:
    
    locations = []
    for ind, beta in enumerate(text):
        if text[ind] == '\n':
            locations.append(ind)
    
    if 0 in locations:
        locations.pop(0)

    i = 0
    while i < len(locations) - 1:
        if locations[i] == locations[i+1] - 1:
            locations.pop(i)
        i += 1

    return len(locations)


print("Example:")
print(non_empty_lines('one simple line\n'))

# These "asserts" are used for self-checking
assert non_empty_lines("one simple line\n") == 1
assert non_empty_lines("") == 0
assert non_empty_lines("\nonly one line\n            ") == 1
assert (
    non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    )
    == 3
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
