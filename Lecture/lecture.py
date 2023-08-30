# """
# Lecture notes and code.

# """

# #           exercise 3

# # from IPython.display import clear_output


# def collect():
#     start = {}
#     while True:
#         name = input("enter name [q to quit]")
#         address = input("enter address")
#         start[name] = address
#         if name == "q":
#             break
#     return start
# print(collect())


def nanda():
    naughty_list = {}
    while True:
        name = input("Enter your name to the naughty list\n[q to quit]: ")
        if name.lower() == "q":
            break
        
        address = input("What address are we skipping this year? ")
        naughty_list[name] = address
        
    return naughty_list

print(nanda())
