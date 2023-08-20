"""
Code challenge: Repeat the characters

Create a Python function that accepts a string.
The function should return a string, with each character in the original string doubled.
If you send the function “now” as a parameter, it should return “nnooww,” 
and if you send “123a!”, it should return “112233aa!!”.
"""
def repeat_character(string_value):

    if not isinstance(string_value, str):
        raise ValueError("The argument value must be a string.")

    return ''.join([char*2 for char in string_value])


if __name__ == '__main__':

    test_value = 'now'
    result = repeat_character(test_value)
    print(f"Original: {test_value} | Doubled: {result}")
