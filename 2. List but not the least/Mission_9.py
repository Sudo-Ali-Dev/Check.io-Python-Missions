# https://py.checkio.org/en/mission/backward-each-word/

def backward_string_by_word(text: str) -> str:

    reversed_text = []
    new_text = text.split(" ")
    for words in new_text:
        reversed_text.append(words[::-1])
    return " ".join(reversed_text)

print("Example:")
print(backward_string_by_word("world"))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")
