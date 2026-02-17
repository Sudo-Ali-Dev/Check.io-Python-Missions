# https://py.checkio.org/en/mission/all-upper/

def is_all_upper(text: str) -> bool:
    remove_spaces = text.replace(" ", "")
    new_text = "".join(remove_spaces)

    if new_text == "":
        return True
    
    for alpha in new_text:
        if alpha.islower():
            return False

    return True


print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
