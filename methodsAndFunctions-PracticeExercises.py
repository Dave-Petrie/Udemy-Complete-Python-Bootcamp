# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

# This is Coding Exercise. They want me to use Jupter Notebooks but I don't like using it. 

#
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
#

def lesser_of_two_evens(a,b):
    if a%2 + b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

#
# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#

def animal_crackers(text):
    wordlist = text.lower().split()

    return wordlist[0][0] == wordlist[1][0]

#
# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#

def makes_twenty(n1,n2):
    if sum(n1,n2) == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False