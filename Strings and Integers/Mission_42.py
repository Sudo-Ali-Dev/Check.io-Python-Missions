# https://py.checkio.org/en/mission/most-wanted-letter/

def checkio(text: str) -> str:

    list = []

    for alpha in text.lower():
        if alpha.isalpha():
            list.append(alpha)

    new_text = "".join(list)

    new_list = []

    i = 0
    while i < len(new_text):
        occurrence = 0
        for alpha in new_text:
            if new_text[i] == alpha:
                occurrence += 1
        new_list.append(occurrence)
        i += 1

    max_occ = max(new_list)

    final_list = []
    
    j = 0
    while j < len(new_text):
        
        occurrence = 0
        
        for alpha in new_text:
        
            if new_text[j] == alpha:
                occurrence += 1
        if occurrence == max_occ:
            final_list.append(new_text[j])
        
        j += 1


    return min(final_list)

print("Example:")
print(checkio("AAaooo!!!!"))

# These "asserts" are used for self-checking
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")
