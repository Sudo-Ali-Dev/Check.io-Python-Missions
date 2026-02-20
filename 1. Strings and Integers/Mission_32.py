# https://py.checkio.org/en/mission/longest-common-prefix/

def longest_prefix(arr: list[str]) -> str:



    lenWord = []
    common = []
    tempCommon = []
    
    for word in arr:
        lenWord.append(len(word))
    
    loopTimes = min(lenWord)

    i = 0
    j = 0
    k = 0
    l = 2


    if len(arr) == 1: # for one element in string
        common = arr
        return "".join(common)
    
    elif len(arr) == 2: # for Two elements in string
        while(i < loopTimes):
            
            if arr[0][i] == arr[1][i]:
                common.append(arr[0][i])
            else: 
                return "".join(common)
            
            i += 1
        return "".join(common)
    
    elif len(arr) >= 3: # for three or more than elements in string
    
        while(i < loopTimes):
            
            if arr[0][i] == arr[1][i]:
                common.append(arr[0][i])
            
            i += 1

        while(j < (len(arr) - 2)):
            while (k < len(common)):
                if common[k] == arr[l][k]:
                    tempCommon.append(common[k])
                else: 
                    return "".join(tempCommon)
                k = k + 1
            j += 1
            l += 1
        
        return "".join(tempCommon)



print("Example:")
print(repr(longest_prefix(["interspace", "interface", "interstellar", "intersperse"])))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")
