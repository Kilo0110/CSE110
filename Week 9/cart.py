
options = ["1. Add new item", "2. View cart",
           "3. Remove item", "4. Compute total", "5. Quit"]


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
    user_input = int(input("Your option: "))
    return user_input
# end def


cart = []


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"['{self.name}', {self.price}]"


print_options(options)
selected_option = get_user_input()


def evaluate_option(selected_option, cart):
    """
    Purpose: Evaluates the user's option and performs actions based on it
    """
    if selected_option == 1:
        new_item_name = input("What item would you like to add? ")
        new_item_price = input(f"What is the price of '{new_item_name}'? $")
        new_item = Item(new_item_name, + new_item_price)
        cart.append(new_item)
        print(f"Item '{new_item_name}' has been added to the cart.")
        print_options(options)
        selected_option = get_user_input()
        evaluate_option(selected_option, cart)
    if selected_option == 2:
        if cart:
            for item in cart:
                # comment: Print out the items in the cart
                print(f"{cart.index(item) + 1}. {item.name} - ${item.price}")
            # end for
        else:
            print(f"No items in the cart")
        print_options(options)
        selected_option = get_user_input()
        evaluate_option(selected_option, cart)
    if selected_option == 3:
        item_to_remove = int(input("Which item would you like to remove? "))
        if item_to_remove > len(cart):
            print("Sorry, that is not a valid item number")
        else:
            del cart[item_to_remove - 1]
            print("Item removed")
        print_options(options)
        selected_option = get_user_input()
        evaluate_option(selected_option, cart)
    if selected_option == 5:
        print("Thank you. Goodbye!")
        exit()
# end def


evaluate_option(selected_option, cart)
