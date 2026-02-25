# https://py.checkio.org/en/mission/words-order/

def words_order(text: str, words: list) -> bool:

    if len(words) > 1 and "".join(words) in text:
        return False

    position_ind = []

    i = 0
    while i < len(words):
        
        if words[i] in text:
            position_ind.append(text.index(words[i]))
        else:
            return False
        
        i += 1

    for ind, digit in enumerate(position_ind):
        if (ind + 1) >= len(position_ind):
            break
        if digit >= position_ind[ind+1]:
            return False
    
    return True

print("Example:")
print(words_order("hi world im here", ["world"]))

# These "asserts" are used for self-checking
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False
assert words_order("hi world im here", ["world", "im", "here"]) == True
assert words_order("hi world im here", ["world", "hi", "here"]) == False
assert words_order("hi world im here", ["world", "world"]) == False
assert words_order("hi world im here", ["country", "world"]) == False
assert words_order("hi world im here", ["wo", "rld"]) == False
assert words_order("", ["world", "here"]) == False
assert words_order("hi world world im here", ["world", "world"]) == False
assert (
    words_order("hi world world im here hi world world im here", ["world", "here"])
    == True
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
