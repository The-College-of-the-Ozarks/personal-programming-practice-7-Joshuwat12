# lists.py
#
# Defines average and largest functions
# Inputs a list from the user
# Outputs the average and largest element of the list


# Functions
def average(l):
  total = 0
  for i in l:
    total += i
  return total / len(l)

# TODO: COMPLETE THIS DEFINITION
def largest(l):
  m = l[0]
  for i in l[1:]:
    if i > m:
      m = i
  return m


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