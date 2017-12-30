print("**************************** \n The script loaded fine. Please note this is working with Python 3. \n ****************************")

print ('ASSESSMENT PIECE 1 \n')

#Question 1 - Numbers
print ('\n QUESTION 1 \n **********')
x = ((10**2)+(10*10))/2+0.5-0.25
print(x)

#Question 2 - Strings
print ('\n QUESTION 2 \n **********')

s = 'hello'
print(s[1])
print(s[4]+s[3]+s[2]+s[1]+s[0])
print(s[4])
print(s[4:])

#Question 3 - Lists
print ('\n QUESTION 3 \n **********')

    #build a list two different ways
my_list1 = [0, 0, 0, 0]
my_list1_0 = 0
my_list1_1 = 0
my_list1_2 = 0
my_list1_3 = 0
print(my_list1)
print([my_list1_0, my_list1_1, my_list1_2, my_list1_3])

    #nested list, output hello
my_list2 = [1,2,[3,4,'hello']]
print(my_list2[2][2])

    # sort the list
my_list3 = [5,3,4,6,1]
my_list3_sorted = sorted(my_list3)
print(my_list3_sorted)

#Question 4 - Dictionaries
print ('\n QUESTION 4 \n **********')

    # pull out hello
dict = {'simple_key':'hello'}
print(dict['simple_key'])

dict = {'k1':{'k2':'hello'}}
print(dict['k1']['k2'])

dict = {'k1':[{'nest_key':['this is deep',['hello']]}]}
var=dict['k1']
dict=var[0]
var=dict['nest_key']
var=var[1]
print(str(var)[2:7])

dict = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print (dict['k1'][2]['k2'][1]['tough'][2][0])

#Question 5 - Tuples
print ('\n QUESTION 5 \n **********')

    #what is the difference between tuples and lists?
print('Tuples are imutable meaning that they cannot be changed once defined')

    #create a tuple
tuple = (1, 2, 3)
print(tuple)

#Question 6 - Sets
print ('\n QUESTION 6 \n **********')

    #what is unique about a set?
print('Sets are unique due to the fact they do not allow duplicate items')

l = [1,2,2,33,4,4,11,22,3,3,2]
print(set(l))

#Question 7 - Boolean
print ('\n QUESTION 7 \n **********')

    #Expression
print(2 > 3)
#Prediction:False

    #Expression
print(3 <= 2)
#Prediction:False

    #Expression
print(3 == 2.0)
#Prediction: False

    #Expression
print(3.0 == 3)
#Prediction: True

    #Expression
print(4**0.5 != 2)
#Prediction: False

    #Final Boolean
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

#True or False?
print(l_one[2][0] >= l_two[2]['k1'])

#Prediction: False

# DO NOT REMOVE

print("**************************** \n End of script \n ****************************")