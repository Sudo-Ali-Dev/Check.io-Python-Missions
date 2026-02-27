# https://py.checkio.org/en/mission/non-empty-lines/

def non_empty_lines(text: str) -> int:

    if "\n" not in text or text == "":
        return 0

    times = []
    for words in text.split(" "):
        if "\n" in words:
            times.append(words)

    if times[0] == text.split(" ")[0] and times[-1] == text.split(" ")[-1]:
        times.pop()

    return len(times)


print("Example:")
print(non_empty_lines("line1\nline2"))

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
