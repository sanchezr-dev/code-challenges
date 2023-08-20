"""
Code challenge: Create a calculator function

Write a Python function that accepts three parameters.
The first parameter is an integer.
The second is one of the following mathematical operators: +, -, /, or .
The third parameter will also be an integer.

The function should perform a calculation and return the results.
For example, if the function is passed 6 and 4, it should return 24.
"""


def calculate(operand_1, operator, operand_2):

    if not (isinstance(operand_1, int) and isinstance(operand_2, int)):
        raise ValueError()

    if not (isinstance(operator, str) and operator in ['+', '-', '/', '*']):
        raise ValueError()

    expression = f"{operand_1} {operator} {operand_2}"

    return eval(expression)


if __name__ == '__main__':

    operand_1 = 6
    operand_2 = 4
    operator = '*'
    result = calculate(operand_1, operator, operand_2)
    print(f"{operand_1} {operator} {operand_2} = {result}")

    operand_1 = 3
    operand_2 = 5
    operator = '-'
    result = calculate(operand_1, operator, operand_2)
    print(f"{operand_1} {operator} {operand_2} = {result}")
