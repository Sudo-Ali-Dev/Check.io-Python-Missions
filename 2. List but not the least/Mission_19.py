# https://py.checkio.org/en/mission/zigzag-array/
# Simple

def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    
    result = []

    i = 0
    while i < rows: # This creates rows.
        result_temp = [] # Saves array of the following iteration
        j = 0
        if i % 2 == 0: # checks if i is even or odd.
            while j < cols: # This creates columns
                result_temp.append(start) # adds value of start to result temp.
                start += 1 # Adds one after each iteration to the start
                j += 1
        else: 
            new_start = (start - 1) + cols # to reverse the order, this deduct one from start as the last value of start is always one more then required.
            start = start + cols # this makes sure that start is updated for the next normal order iteration
            while j < cols:
                result_temp.append(new_start)
                new_start -= 1
                j += 1
        result.append(result_temp) # adds value to the result variable outside of the loops
        i += 1

    return result

print("Example:")
print(create_zigzag(5, 1))

# These "asserts" are used for self-checking
assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]

print("The mission is done! Click 'Check Solution' to earn rewards!")
