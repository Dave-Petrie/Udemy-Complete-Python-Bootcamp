print("**************************** \n The script loaded fine. Please note this is working with Python 3. \n ****************************")

'''
DICTIONARIES

- they are mappings. These are collections of objects sorted by a key
- you can't index a dictionary, you have to call via a key

'''

l = [1, 2, 3]
print(l[0])

my_dict = {'key1':'value', 'key2':'value2', 'k2':100}
print(my_dict['key1'])

#indexing a string
print(my_dict['key1'][1])

#print temporary change
print(my_dict['k2']-50)

#print permanent change
my_dict['k2'] = my_dict['k2']-50
print(my_dict['k2'])

#Nested dictionaries

d = {'k1': {'nestkey': {'subnestkey': 'subnestkeyvalue'}}}
print(d)
print(d['k1'])
print(d['k1']['nestkey'])
print(d['k1']['nestkey']['subnestkey'])
print(d['k1']['nestkey']['subnestkey'].upper())

# Construct a dictionary separately

d2 = {}
d2['k1'] = 5
d2['k2'] = 10
d2['k3'] = 15

print(d2)

# Methods used with dictionaries

print(d2.keys())
print(d2.values())
print(d2.items())

# DO NOT REMOVE

print("**************************** \n End of script \n ****************************")