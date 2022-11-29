# Rite  a  Python  program  that  checks  if  a  string  is  apalindrome,


my_string = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_string = my_string.casefold()

# reverse the string
rev_string = reversed(my_string)

# check if the string is equal to its reverse
if list(my_string) == list(rev_string):

    print("This string is a palindrome.")

