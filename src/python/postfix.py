

# assert solution ("8 2 *") == 8 * 2


def calculate_postfix(postfix_expression):

    value_list = postfix_expression.split(' ')
    numbers = []
    operator = None

    for value in value_list:

        if not value.isnumeric():

            operator = value
            right_operand = numbers.pop()
            left_operand = numbers.pop()
            new_expression = '({} {} {})'.format(
                left_operand, operator, right_operand)
            numbers.append(new_expression)

        else:
            numbers.append(value)

    eval_expression = numbers.pop()
    print(eval_expression)
    return eval(eval_expression)


if __name__ == "__main__":
    postfix_expression = "8 2 *"
    result = calculate_postfix(postfix_expression)
    print(result)

    postfix_expression = "7 2 - 2 *"
    result = calculate_postfix(postfix_expression)
    print(result)

    postfix_expression = "35 7 / 5 -"
    result = calculate_postfix(postfix_expression)
    print(result)

    postfix_expression = "3 2 8 + 9 - *"
    result = calculate_postfix(postfix_expression)
    print(result)
