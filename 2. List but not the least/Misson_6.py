# https://py.checkio.org/en/mission/follow-instructions/

def follow(instructions: str) -> tuple[int, int] | list[int]:
    
    vertical = 0
    horizontal = 0
    destination = []

    
    for direction in instructions:
        if direction == 'f':
            vertical += 1
        elif direction == 'b':
            vertical -= 1
        elif direction == 'r':
            horizontal += 1
        elif direction == 'l':
            horizontal -= 1
        else:
            return 0
    
    destination.append(horizontal)
    destination.append(vertical)

    return destination

print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")

