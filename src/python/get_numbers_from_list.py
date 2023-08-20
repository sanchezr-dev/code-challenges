"""
Code challenge: Just the numbers

Write a function in Python that accepts a list of any length that contains 
a mix of non-negative integers and strings.
The function should return a list with only the integers in the original list in the same order.
"""
def get_numbers_from_list(mixed_list):

    if not all((isinstance(item, int) and item >= 0) \
               or isinstance(item, str) for item in test_list):

        raise ValueError(
            "The list should contain only possitive integer and string values."
        )

    number_list = [item for item in mixed_list if isinstance(item, int)]
    return number_list


if __name__ == '__main__':

    test_list = [1, 2, 'A', 'BB', 'CCC', 3]
    filtered_list = get_numbers_from_list(test_list)
    print(f"Original list: {test_list} | Numbers: {filtered_list}")

    test_list = [10, 5, 'A', 'BB', 99, 'CCC', 3]
    filtered_list = get_numbers_from_list(test_list)
    print(f"Original list: {test_list} | Numbers: {filtered_list}")

    test_list = [10, '100', 3]
    filtered_list = get_numbers_from_list(test_list)
    print(f"Original list: {test_list} | Numbers: {filtered_list}")

    # test_list = [10, 5.5, 9]
    # filtered_list = get_numbers_from_list(test_list)
    # print(f"Original list: {test_list} | Numbers: {filtered_list}")

    # test_list = [10, -99, 3]
    # filtered_list = get_numbers_from_list(test_list)
    # print(f"Original list: {test_list} | Numbers: {filtered_list}")

    # test_list = [10, {0: 'Value'}, 3]
    # filtered_list = get_numbers_from_list(test_list)
    # print(f"Original list: {test_list} | Numbers: {filtered_list}")
