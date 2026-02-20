# https://py.checkio.org/en/mission/the-longest-word/

def longest_word(sentence: str) -> str:


    if sentence == "" or not sentence[0].isalpha():
        return ""

    lengthStr = []
    for words in sentence.split():
        wordLength = 0
        for alpha in words:
            wordLength += 1
        lengthStr.append(wordLength)
    
    maxLengthStr = max(lengthStr)

    for words in sentence.split():
        wordLength = 0
        for alpha in words:
            wordLength += 1
        if maxLengthStr == wordLength:
            return words



print("Example:")
print(longest_word(""))

# These "asserts" are used for self-checking
assert longest_word("hello world") == "hello"
assert longest_word("openai gpt-4") == "openai"
assert longest_word("this is a sentence") == "sentence"
assert longest_word("the quick brown fox") == "quick"
assert longest_word("jumped over the lazy dog") == "jumped"
assert longest_word("typescript is great") == "typescript"
assert longest_word("the answer is 42") == "answer"
assert longest_word("to be or not to be") == "not"
assert longest_word("that is the question") == "question"
assert longest_word("") == ""
assert longest_word(" ") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
