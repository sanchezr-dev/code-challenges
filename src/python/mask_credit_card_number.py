"""
Code challenge: Hide the credit card number.

Write a function in Python that accepts a credit card number.
It should return a string where all the characters are hidden with an asterisk except the last four.
For example, if the function gets sent “4444444444444444”, then it should return “4444”.
"""


import re


def mask_cc_number(cc_number, digits_to_keep=4, mask_char='*'):

    if not (cc_number and isinstance(cc_number, str)):
        raise ValueError('The credit card number argument must be a string.')

    if not any(char.isdigit() or char.isspace() for char in cc_number):
        raise ValueError('The credit card number must contain only digits and spaces.')

    total_digits = sum(map(str.isdigit, cc_number))

    if not 16 <= total_digits <= 19:
        raise ValueError(f'The credit card number {cc_number} is invalid.')

    if digits_to_keep >= total_digits:
        raise ValueError(
            f"No enough numbers to mask. \
                Total digits: {total_digits} is less or equal the digis to keep: {digits_to_keep}"
        )

    digits_to_mask = total_digits - digits_to_keep
    masked_cc = re.sub('\d', mask_char, cc_number, digits_to_mask)
    return masked_cc


if __name__ == '__main__':

    cc_number = '1234567890123456'
    print(f"CC: {cc_number} - Masked: {mask_cc_number(cc_number)}")

    cc_number = '0987 6543 2109 8765'
    print(f"CC: {cc_number} - Masked: {mask_cc_number(cc_number)}")

    cc_number = 'ABCD 6543 2109 8765'
    print(f"CC: {cc_number} - Masked: {mask_cc_number(cc_number)}")
