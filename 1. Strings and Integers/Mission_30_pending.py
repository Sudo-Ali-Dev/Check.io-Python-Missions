# https://py.checkio.org/en/mission/count-substring-occurrences/

def count_occurrences(main_str: str, sub_str: str) -> int:

    count = 0

    splitMainStr = main_str.split()
    newMianStr = "".join(splitMainStr)
    splitSubStr = sub_str.split()
    newSubStr = "".join(splitSubStr)
    lenSubStr = len(newSubStr)


    j = 0
    for i, alphas in enumerate(newMianStr):
        if j < lenSubStr:
            if newMianStr[i] == newSubStr[j]:
                count += 1
        elif j >= lenSubStr:
            j = 0
            if newMianStr[i] == newSubStr[j]:
                count += 1
        j += 1
    return count


print("Example:")
print(count_occurrences("hello world hello", "o w"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
