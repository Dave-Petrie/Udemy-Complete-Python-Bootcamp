print("**************************** \n The script loaded fine. Please note this is working with Python 3. \n ****************************")

'''
FOR LOOPS

for item in object
    statements to do stuff
'''
l = [1,2,3,4,5]
for element in l:
    print(element)

# % used as MODULAR which is basically remainer from a division

print('The remainder when 10 is divided by three is', 10%3)

# Print out even and odd numbers from list

for numbers in l:
    if numbers % 2 != 0:
        print(numbers,'Is odd')
    elif (numbers % 2) == 0:
        print(numbers,'Is even')
    else:
        print('error')

# Sum list
list_sum = 0

for numbers in l:
    list_sum = list_sum + numbers

print(list_sum)

# What is a string?

string = 'This is a string\n'

for letter in string:
    print(letter)

#Can you do this with a typol?

tupol = (1, 2, 3, 4, 5)
for item in tupol:
    print(item)

# a list of tupols

my_list = [(1,2),(6,9),(10,12)]
for tup in my_list:
    print (tup)
for (t1,t2) in my_list:
    print (t1)

# Dictionaries
my_dict = {'key1':'value', 'key2':'value2', 'k2':100}

for k,v in my_dict.items():
    print('k is %s and v is %s' %(k,v))

# DO NOT REMOVE

print("**************************** \n End of script \n ****************************")