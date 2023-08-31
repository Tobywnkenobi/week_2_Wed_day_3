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



def groceries():
    shopping_list = {}
    while True:
        name = input("What food are you in need of? \n[q to quit]: ")
        if name.lower() == "q":
            break
        
        quantity = input("How many would you like? ")
        shopping_list[name] = quantity
        
    return shopping_list

print(groceries())
