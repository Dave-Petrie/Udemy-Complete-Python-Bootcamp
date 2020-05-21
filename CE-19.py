# This is Coding Exercise 19: Skyline

# Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase.

def myfunc(input_string):
   #Every second letter is going to need to be converted to uppercase. Every odd letter is going to need to be lowercase.
   lowercase_input = input_string.lower()
   result = ""
   for index, letter in enumerate(lowercase_input):
        if index % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()
   return result