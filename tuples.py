print("**************************** \n The script loaded fine. Please note this is working with Python 3. \n ****************************")

'''
TUPLES

- They are unique due to being immutable. This means you cannot change what is in there already. 

'''

t = (1, 2, 3, "cat")
print(t)
print(t[1])

print(t.index('cat'))

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list[1] = 'changed'
# my_tuple[1] = 'changed' <-- gets an error which is expected

# DO NOT REMOVE

print("**************************** \n End of script \n ****************************")