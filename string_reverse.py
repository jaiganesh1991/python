def string_reversion_function_for_loop(string_to_reverse):
    """THis function uses for loop to reverse"""
    reverse_string = ""
    for char in string_to_reverse:
        reverse_string = char + reverse_string
    return reverse_string

def string_reversion_function_inbuilt(string_to_reverse):
    """This function uses the inbuilt function of reversed"""
    return "".join(reversed(string_to_reverse))

def string_reversion_function_slice(string_to_reverse):
    """This function uses the slicing function """
    return string_to_reverse[::-1] 
