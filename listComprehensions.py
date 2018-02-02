print("**************************** \n The script loaded fine. Please note this is working with Python 3. \n ****************************")

'''
COMPREHENSIONS

THis is a test addition
        
'''
l = []
for letter in 'word':
    l.append(letter)
print(l)

lst = [letter for letter in 'word']
print(lst)

lst2 = [x**2 for x in range(0,11)]
print(lst2)

lst3 = [number for number in range(11) if number % 2 == 0] #Remeber that % is divide so this 

# DO NOT REMOVE

print("**************************** \n End of script \n ****************************")