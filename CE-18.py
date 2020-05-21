# This is Coding Exercise 18: Pick evens

# Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.

def myfunc(*args):
    even_numbers = list(filter(lambda x: (x % 2 == 0), args))
    return even_numbers