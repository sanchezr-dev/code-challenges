"""

Code challenge: Unique characters in a string.

Write a function that determines if any given string has all unique characters,
(i.e. no character in the string is duplicated).

If the string has all unique characters, print "all unique".

If the string does not have all unique characters, print "duplicates found".
"""


def check_uniques_and_duplicates_chars(str_value: str) -> str:

    normalized_str_value = str_value.replace(' ', '').lower()
    unique_chars = set(normalized_str_value)
    unique_count = len(unique_chars)

    if unique_count == len(normalized_str_value):
        result = "All unique."
    else:
        result = "Duplicates found."

    # Print values only for testing.
    print(f"Original: {str_value}")
    print(f"Normalized: {normalized_str_value}")
    print(f"Unique chars: {unique_chars}")
    print(f"Unique count: {unique_count}")
    print(f"Evaluation: {result}\n")

    return result


def check_uniques_and_duplicates_chars_2(str_value: str) -> str:

    normalized_str_value = str_value.replace(' ', '').lower()
    parsed_chars = {}

    for char in normalized_str_value:

        if parsed_chars.get(char):
            return "Duplicates found."

        parsed_chars[char] = True

    return "All unique."


if __name__ == '__main__':

    test_data = 'ABC DEF'
    check_uniques_and_duplicates_chars(test_data)
    evaluation = check_uniques_and_duplicates_chars_2(test_data)
    print(f"Original: {test_data} | Evaluation: {evaluation}\n\n")

    test_data = 'Lorem Ipsum'
    check_uniques_and_duplicates_chars(test_data)
    evaluation = check_uniques_and_duplicates_chars_2(test_data)
    print(f"Original: {test_data} | Evaluation: {evaluation}\n\n")

    test_data = 'abc $%& 123  AB3'
    check_uniques_and_duplicates_chars(test_data)
    evaluation = check_uniques_and_duplicates_chars_2(test_data)
    print(f"Original: {test_data} | Evaluation: {evaluation}\n\n")
