"""
Word frequency
Given a list of words, return a dictionary where the keys are the unique words and values are the number of times each word appears.

Input: list of strings:
output: dictionary:
"""
# {'item': count}
# def grocery_quantities(grocery_list):
#     hash_map = {}
#     for item in grocery_list:
#         if item in hash_map:
#             hash_map[item] +=1
#         else:
#             hash_map[item] = 1
#     return hash_map





def grocery_quantities(grocery_list):
    hash_map = {}
    for item in grocery_list:
        hash_map[item] = hash_map.get(item, 0) + 1
    return hash_map

print(grocery_quantities(["apple", "banana", "apple", "orange", "banana", "apple"]))

