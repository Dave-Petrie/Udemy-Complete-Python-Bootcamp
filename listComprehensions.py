print("**************************** \n The script loaded fine. Please note this is working with Python 3. \n ****************************")

'''
COMPREHENSIONS
        
'''
l = []
for letter in 'word':
    l.append(letter)
print(l)

lst = [letter for letter in 'word']
print(lst)

lst2 = [x**2 for x in range(0,11)]
print(lst2)

lst3 = [number for number in range(11) if number % 2 == 0] #Remember that % is divide so this
print(lst3)

lst4 = []
for number in range(11):
    if number %2 == 0:
        lst4.append(number)
        print(lst4)
print(lst4)

celsius = [0,10,20,1,34.5]
fahrenheit = [(temp*(9/5.0)+32) for temp in celsius]
print(celsius)
print(fahrenheit)

#Nesting lists into other lists
lst5 = [x**2 for x in [x**2 for x in range(11)]]
print(lst5)

# DO NOT REMOVE

print("**************************** \n End of script \n ****************************")