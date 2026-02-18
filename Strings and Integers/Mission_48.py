# https://py.checkio.org/en/mission/middle-characters/

def middle(text: str) -> str:

    text_length = len(text)

    if text_length % 2 == 1:
        half = (text_length // 2)
        return text[half]
    else:
        half = (text_length // 2) - 1
        return text[half : (half + 2)]


print("Example:")
print(middle("test"))

# These "asserts" are used for self-checking
assert middle("example") == "m"
assert middle("test") == "es"

print("The mission is done! Click 'Check Solution' to earn rewards!")
