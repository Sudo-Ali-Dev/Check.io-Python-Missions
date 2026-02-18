# https://py.checkio.org/en/mission/longest-substring-of-unique-characters/

def longest_substr(s: str) -> int:

    full = []
    result = []
    
    i = 0
    h = 0

    while True:

        if h >= len(s): 
            break

        if s[i] not in result:
            result.append(s[i])
            i += 1
        else: 
            full.append(len(result))
            result = []
        

    return max(full)


print("Example:")
print(longest_substr("pwwkew"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
