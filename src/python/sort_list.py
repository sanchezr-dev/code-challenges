"""
Challenge: Sort a list.

Create a function in Python that accepts two parameters.
The first will be a list of numbers.
The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is “asc,” then the function should return a list with the numbers in ascending order.
If it's “desc,” then the list should be in descending order, and if it's “none,” it should return the original list unaltered.
"""


def sort_list(original_list, ordering):
    """
    Function to sort a list.

    Args:
        original_list: Original list to be sorted.
        ordering: Sort order to apply.
    
    Returns:
        list: A new sorted copy of the list.
    """

    if ordering is None:
        sorted_list = original_list[:]

    elif ordering == 'asc':
        sorted_list = sorted(original_list)

    elif ordering == 'desc':
        sorted_list = sorted(original_list, reverse=True)

    else:
        raise ValueError(
            "The ordering param can only accept the values: 'asc', 'desc', and 'None'")

    return sorted_list


def print_results(original_list, sorted_list):
    """
        Prints the original list and the sorted list.
    """
    print(f'Original: {original_list} - Result: {sorted_list}')


if __name__ == '__main__':

    original_list = [5, 1, 3, 4, 2]

    result = sort_list(original_list, ordering='asc')
    print_results(original_list, result)

    result = sort_list(original_list, ordering='desc')
    print_results(original_list, result)

    result = sort_list(original_list, ordering=None)
    print_results(original_list, result)
