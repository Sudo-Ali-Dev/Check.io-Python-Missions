# https://py.checkio.org/en/mission/fuzzy-string-matching/

def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:

    sameSameButDifferent = 0

    min_length = min(len(str1), len(str2))

    for i in range(min_length):
        if str1[i] != str2[i]:
            sameSameButDifferent += 1

    sameSameButDifferent += abs(len(str1) - len(str2))

    if sameSameButDifferent <= threshold:
        return True
    else:
        return False


print("Example:")
print(fuzzy_string_match("hello world", "hxllo world", 0))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
