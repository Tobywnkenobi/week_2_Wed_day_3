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

def grocery_quantities(grocery_list):
    # {'item': count}
    hash_map = {}
    for item in grocery_list:
        if item in hash_map:
            hash_map[item] += 1
        else:
            hash_map[item] = 1
    return hash_map

def grocery_quantities3(grocery_list):
    # {'item': count}
    hash_map = {}
    for item in grocery_list:
        hash_map[item] = hash_map.get(item, 0) + 1
    return hash_map

def grocery_quantities2(grocery_list):
    # {'item': count}
    hash_map = {}
    for item in grocery_list:
        if item not in hash_map:
            hash_map[item] = 0
        hash_map[item] += 1
    return hash_map