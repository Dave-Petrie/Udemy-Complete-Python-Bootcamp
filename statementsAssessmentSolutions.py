print("**************************** \n The script loaded fine. Please note this is working with Python 3. \n ****************************")

'''
STATEMENTS ASSESSMENT
        
'''

#use for, split() and if to create a statement that will print out letters that start with 's'

st='Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print (word)

#Use range() to print all the event numbers from 0 to 10

answer = list(range(0,11,2))
print(answer)

#Use List comprehension to create a list of all numbers between 1 and 50 that are dividisble by 3

answer2 = [x for x in range(50) if x%3 == 0]
print (answer2)

#Go through the string below and if the length of a word is even, print "even!"

st = 'print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word)%2 ==0:
        print (word+" <-- has an even length!")

#Write a program that prints the integers from 1 to 100. But for multiples of three, print "Fizz" instead of the numbers, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"

for num in list(range(1,101)):
    if num % 5 == 0 and num % 3 == 0:
        print ("FizzBuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)

# Use list comprehension to create a list of the first lettesr of every word in the string below

st = 'Create a list of the first letters of every word in this string'
print( [word[0] for word in st.split()] )


# DO NOT REMOVE

print("**************************** \n End of script \n ****************************")