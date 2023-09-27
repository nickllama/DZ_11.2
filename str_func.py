def convert_to_uppercase(input_string):
    "Convert to uppercase"
    return input_string.upper()

def capitalize_first_letters(input_string):
    """
    Capitalize the first letter of each word in the input string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The input string with the first letter of each word capitalized.
    """
    return " ".join(word[0].upper() + word[1:] if len(word) > 0 else '' for word in 
input_string.split())
