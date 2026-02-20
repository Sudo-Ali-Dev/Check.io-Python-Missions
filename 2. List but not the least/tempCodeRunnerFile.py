    new_list = []
    
    i = 0
    while i < len(array):
        new_list.append(array[i])
        i += 2

    final_digit = array[-1]    

    result = sum(new_list) * final_digit

    return result