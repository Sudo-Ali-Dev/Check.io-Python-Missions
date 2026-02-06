# https://py.checkio.org/en/mission/goes-right-after-simplified/

def goes_after(word: str, first: str, second: str) -> bool:
    firstSecond = (first, second)
    joinedFirstSecond = "".join(firstSecond)
    return True if joinedFirstSecond in word else False
    
print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
