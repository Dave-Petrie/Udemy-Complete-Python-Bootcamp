print("**************************** \n The script loaded fine. Please note this is working with Python 3. \n ****************************")

'''
FILES

- Generally need to import stuff in order to work with files

'''

f = open('test.txt')
print(f.read())

# the python "cursor" is now at the bottom of the file. Therefore, it needs to be reset.abs
print(f.read())
f.seek(0)
print(f.read())

#iterate through a text file

for line in open('test2.txt'):
    print (line)

# DO NOT REMOVE

print("**************************** \n End of script \n ****************************")