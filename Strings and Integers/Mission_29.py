# https://py.checkio.org/en/mission/bird-language/

def translation(text: str) -> str:
    vowels = "aeiou"
    word = []

    for i, alphas in enumerate(text):
        if alphas not in vowels:
            word.append(text[i])
            i = i + 2
        else: 
            word.append(text[i])
            i = i + 3

    return word


print("Example:")
print(translation("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")