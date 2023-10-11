# 1) Build a Shopping Cart

# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list        USE DICTIONARY
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list 

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

""" Problem: Word Frequency
Prompt:
Given a list of words, return a dictionary where the keys are the unique words and the values are the number of times each word appears.
Input:
A list of strings.
Output:
A dictionary.
Example:

Input: ["apple", "banana", "apple", "orange", "banana", "apple"]
Output: {"apple": 3, "banana": 2, "orange": 1}
Bonus:
- Can you handle the case where the word capitalization is mixed, e.g., "Apple" and "apple" should be treated as the same word?
- Can you handle punctuation and white spaces?
 """



# def groceries():
#     shopping_list = {}
#     while True:
#         name = input("What food are you in need of? \n[q to quit]: ")
#         if name.lower() == "q":
#             break
        
#         quantity = input("How many would you like? ")
#         shopping_list[name] = quantity
        
#     return shopping_list

# print(groceries())

# Build A Shopping Cart

def check_user_shopping():
    user_shopping = input('Are you shopping? [y]es/[n]o?: ').lower()
    return True if user_shopping in 'yes' else False

def get_user_input():
    return input('What do you want to do? [a]dd,[d]elete,[s]howJ?: ').lower()
    
def add_to_cart(shopping_cart, item, price, quantity):
    if item not in shopping_cart:
      shopping_cart[item] = {
          'price': price,
          'quantity': quantity
      }
    else:
        shopping_cart[item]['quantity'] += quantity

def del_from_cart(shopping_cart, item):
    if item in shopping_cart:
      del shopping_cart[item]
    else:
        print('Item not in cart')

def display_cart(shopping_cart):
    total_price = 0
    for item, dict in shopping_cart.items():
      print(f'{item}\nquantity: {dict["quantity"]}\nprice: {dict["price"]}')
      total_price += dict["quantity"] * dict["price"]
    print(f'Total Price: {total_price:.2f}')

def driver(shopping_cart):
    while check_user_shopping():
        user_input = get_user_input()
        if user_input == 'a':
            item = input("what are we adding?: ")
            while True:
              try:
                price = float(input('What is price of item?: '))
                break
              except:
                 print("Please enter price in digits. Ex: 10.99")
            while True:
              quantity = input("How many are you adding? ")
              if quantity.isdigit():
                 quantity = int(quantity)
                 break
              else:
                 print("Please enter quantity in digits. Ex: 10")
            add_to_cart(shopping_cart, item, price, quantity)
        elif user_input == 'd':
            user_delete_option = input("what item are you deleting?: ")
            del_from_cart(shopping_cart, user_delete_option)
        elif user_input != 's':
            print('please enter valid option')
        display_cart(shopping_cart)

test_cart = {}
driver(test_cart)