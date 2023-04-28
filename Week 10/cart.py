from decimal import Decimal
import os

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"['{self.name}', {self.price}]"


options = ["1. Add new item", "2. View cart",
           "3. Remove item", "4. Compute total", "5. Clear screen", "6. Quit"]


def print_options(options):
    """
    Purpose: Print the user options
    """
    print()
    print("Please select one of the following:")
    for option in options:
        # comment: Print the options
        print(option)
    # end for
# end def


def get_user_input():
    """
    Purpose: Gets the user's input and returns it
    """
    user_input = input("Your option: ")
    return user_input
# end def

def add_new_item():
    """
    Purpose: Add a new item to the cart
    """
    new_item_name = input("What item would you like to add? ")
    new_item_price = input(f"What is the price of '{new_item_name}'? $")
    new_item = Item(new_item_name, new_item_price)
    cart.append(new_item)
    print(f"\nItem '{new_item_name}' has been added to the cart.")
# end def

def print_items_in_cart(cart):
    """
    Purpose: Print out the items in the cart if there's any
    """
    if cart:
        for item in cart:
            # comment: Print out the items in the cart
            item_price = item.price
            formatted_price = Decimal(item_price).quantize(Decimal('0.00'))
            print(f"\n{cart.index(item) + 1}. {item.name} - ${formatted_price}")
        # end for
    else:
        print(f"\nNo items in the cart.")
# end def

def remove_item_from_cart(cart):
    """
    Purpose: Remove specified item from the cart
    """
    if cart:
        item_to_remove = int(input("Which item would you like to remove? "))
        if item_to_remove > len(cart):
            print("\nSorry, that is not a valid item number.")
        else:
            del cart[item_to_remove - 1]
            print("\nItem removed")
    else:
        print(f"\nSorry, your cart is empty.")
# end def

def compute_total_amount(cart):
    """
    Purpose: Computes the total amount of the items in the cart
    """
    if cart:
            total_amount_in_cart = 0
            for item in cart:
                # comment: Add up all items in the cart and display it
                total_amount_in_cart = total_amount_in_cart + int(item.price)
            # end for
            formatted_total = Decimal(total_amount_in_cart).quantize(Decimal('0.00'))
            print(f"\nThe total price of the items in the shopping cart is ${formatted_total}")
    else:
        print(f"\nNo items in cart.")
# end def

cart = []


print_options(options)
selected_option = get_user_input()


def evaluate_option(selected_option, cart):
    """
    Purpose: Evaluates the user's option and performs actions based on it
    """

    try:
        # comment: Checks if the user input is a number or if it can be safely converted to a number
        user_option = int(selected_option)
    except ValueError:
        print("Please input ONLY numbers.")

        print_options(options)
        selected_option = get_user_input()
        evaluate_option(selected_option, cart)
    # end try

    if user_option == 1:
        add_new_item()

        print_options(options)
        selected_option = get_user_input()
        evaluate_option(selected_option, cart)

    if user_option == 2:
        print_items_in_cart(cart)

        print_options(options)
        selected_option = get_user_input()
        evaluate_option(selected_option, cart)

    if user_option == 3:
        remove_item_from_cart(cart)

        print_options(options)
        selected_option = get_user_input()
        evaluate_option(selected_option, cart)

    if user_option == 4:
        compute_total_amount(cart)

        print_options(options)
        selected_option = get_user_input()
        evaluate_option(selected_option, cart)

    if user_option == 5:
        os.system("clear")

        print_options(options)
        selected_option = get_user_input()
        evaluate_option(selected_option, cart)

    if user_option == 6:
        print("Thank you. Goodbye!")
        exit()
    else:
        print('You have an entered an invalid option')
        selected_option = get_user_input()
        evaluate_option(selected_option, cart)
        
# end def


evaluate_option(selected_option, cart)
