# https://py.checkio.org/en/mission/cut-sentence/

def cut_sentence(line: str, length: int) -> str:

    if len(line) <= length:
        return line
    
    if line[length] == " ":
        return line[:length] + "..."
    
    if len(line.split()[0]) > length:
        return "..."
    
    extracted_sentence = []
    
    i = 0
    while i < length:
        extracted_sentence.append(line[i])
        i += 1
    
    join_ext_sen = "".join(extracted_sentence)[::-1] # joined and reversed
    indexed = join_ext_sen.find(" ")
    reversed_ext = join_ext_sen[indexed::]
    restored_text = reversed_ext[::-1]

    if restored_text.endswith(" "):
        restored_text = restored_text[:-1] + "..."

    return restored_text


print("Example:")
print(cut_sentence("Hi my name is Alex", 1))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")
