print("**************************** \n The script loaded fine. Please note this is working with Python 3. \n ****************************")

'''
LISTS

- lists don't have size or type constraints

'''
myList = [1, 2, 3]

print (myList)
print (len(myList))

mySecondList = ['one', 'two', 'three', 4, 5]
print (mySecondList[0])
print (mySecondList[3])
print (mySecondList[2])
print (mySecondList[2:])
print (mySecondList[:3])

#Can concatenate lists as well
print(myList+mySecondList)

# Can add to existing or new lists with older ones

myThirdList = myList + mySecondList + ['What is going on here?']
print (myThirdList)

# Methods for lists

l = [1, 2, 3]

    # Append method

l.append('append me! please')
print (l)
print (l.pop())
print (l)

# Changing the order of lists

l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l_3 = [7, 8, 9]

l_1_sort = l_1.sort()
l_2_reverse = l_2.reverse()
matrix = [l_1, l_2, l_3]









# DO NOT REMOVE

print("**************************** \n End of script \n ****************************")