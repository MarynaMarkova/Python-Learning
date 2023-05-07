print(
    """
WELCOME TO OUR USELESS STORE!
*****************************"""
)

item = input("what item are you purchasing? ")
price = float(input(f"what is the price of a {item}?"))
quantity = int(input(f"how many {item}s are you buying?"))

print(
    f"""
Added {quantity} {item}(s) to shopping cart.
Subtotal: ${price*quantity}
"""
)
