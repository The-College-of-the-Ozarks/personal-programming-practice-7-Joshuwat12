# lists.py
#
# Defines average and largest functions
# Inputs a list from the user
# Outputs the average and largest element of the list


# TODO: COMPLETE THIS DEFINITION
def average(l):
    pass

# TODO: COMPLETE THIS DEFINITION
def largest(l):
    pass


# Inputs the list from the user as a string
l = input("Input the list as numbers with separated by spaces and/or commas in between.\n\n")

# Turns commas into spaces for splitting
l = l.replace(',',' ')

# Turns the string into a list by breaking apart at spaces
l = l.split(' ')

# Removes any empty strings from the list (caused by putting multiple spaces and/or commas in the input)
while '' in l:
    l.remove('')

# Cast each entry of the list (currently a string) to a float
for i in range(len(l)):
    l[i] = float(l[i])


# Calling each function on the list l and outputting the results
print("\nThe input list was read as " + str(l))
print("\nThe average of the list is " + str(average(l)))
print("\nThe largest element of the list is " + str(largest(l)))
