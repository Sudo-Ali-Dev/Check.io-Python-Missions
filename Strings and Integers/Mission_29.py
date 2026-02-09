# https://py.checkio.org/en/mission/bird-language/

def translation(text: str) -> str:
    vowels = "aeiouy"
    word = []
    j = 0

    for i, alphas in enumerate(text):

        if j != i:
            continue

        if alphas == " ":
            word.append(text[i])
            j += 1
            continue

        if alphas not in vowels:
            word.append(text[i])
            j = j + 1            
        elif alphas in vowels: 
            word.append(text[i])
            j = j + 2

        j += 1

    return "".join(word)


print("Example:")
print(translation("sooooso aaaaaaaaa"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")