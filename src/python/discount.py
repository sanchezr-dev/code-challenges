"""
Code challenge: Give me the discount.
Create a function in Python that accepts two parameters.
The first should be the full price of an item as an integer.
The second should be the discount percentage as an integer.

The function should return the price of the item after the discount has been applied.
For example, if the price is 100 and the discount is 20, the function should return 80.
"""


def get_price_with_discount(price, discount_percentage):

    if not (isinstance(price, int) and isinstance(discount_percentage, int)):
        raise ValueError("Price and Discount arguments should be integers.")

    return price - (price * (discount_percentage / 100))

if __name__ == '__main__':

    price = 100
    discount_percentage = 15
    price_with_discount = get_price_with_discount(price, discount_percentage)
    print(f"Price: {price} | Price with discount: {price_with_discount}")
