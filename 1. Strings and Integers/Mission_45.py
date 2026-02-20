# https://py.checkio.org/en/mission/conversion-from-camelcase/

def from_camel_case(name: str) -> str:
    
    result = []
    length = len(name)
    for i, alpha in enumerate(name):

        if (i + 1) >= length:
            result.append(name[i])
            break

        if alpha.isupper():
            result.append(alpha)
            if name[(i+1)].isupper():
                result.append(" ")
        elif alpha.lower():
            result.append(alpha)
            if name[(i+1)].isupper():
                result.append(" ")
        else:
            return "Error in processing"

    final_result = "".join(result).replace(" ", "_").lower()

    return final_result
    
print("Example:")
print(from_camel_case("IPhone"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
