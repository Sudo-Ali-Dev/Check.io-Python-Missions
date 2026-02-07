# https://py.checkio.org/en/mission/three-words/

def checkio(words: str) -> bool:

    sum = 0
    
    for word in words.split():
        if word.isalpha():
            sum += 1
            if sum == 3:
                return True
        else:
            sum = 0

    return False


print("Example:")
print(checkio("He is 123 man"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
