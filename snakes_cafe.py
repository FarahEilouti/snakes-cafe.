print("""
******************************************
**      Welcome to the Snakes Cafe!     **
**      Please see our menu below.      **
**                                      **
**  To quit at any time, type "quit"    **
******************************************
""")

menu = {
"Appetizers": ["Wings", "Cookies", "Spring Rolls"],
"Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
"Desserts": ["Ice Cream", "Cake", "Pie"],
"Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

# to pretty print the menu
for key, value in menu.items():
    print(key)
    print("----------")
    for food in value:
        print(food)
    print()

print("""
**************************************
**  What would you like to order?   **
**************************************
""")

user_input = ""
order_counter = 0
order_summery = [] 

while user_input != "quit":
    user_input = input("> ")
    print()

    if user_input != 'quit':
        order_summery.append(user_input)
        order_counter += 1
        print(f"** {order_counter} orders of {user_input} have been added to your meal **")
    else:
        print("The summery of your completer order is:")
        print(order_summery)
