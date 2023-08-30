# Create a function that given a list which represents street lights given as a parameter(l_street), determine if an outage has occurred. A street with a total number of "F" greater than or equal to 2 returns "Outage", anything below returns "Power"
# street: [ 'T', 'F', 'F', 'F' ]				
# Example Output: "Outage"

# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function
# return F>=2 = "outage" 
# else return "power"

#  if/then statement

#WHEW!!


def street(l_street):
    count_f = 0
    for light in l_street:
        if light == 'F':
            count_f += 1
    print(count_f)
    if count_f >= 2:
        return('Outage')
    else:
        return('Power')
print(street (['T', 'F', 'F', 'F']))

"""
Dylan's solutions:

"""

