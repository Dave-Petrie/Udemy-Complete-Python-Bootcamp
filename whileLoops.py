print("**************************** \n The script loaded fine. Please note this is working with Python 3. \n ****************************")

'''
WHILE LOOPS

while test:
    code statement
else:
    final code statement

while test:
    code statement
    if test:
        break
    if test:
        continue
else:
        
'''
x = 0

while x < 10:
    print('The current value of X is', x)
    x += 1
else:
    print('All done :) !')


# Break continue and pass
y = 0

while y < 10:
    print('\nThe current value of Y is', y)
    print('\nY is still less than 10, adding 1 to Y')
    y += 1
    if y == 7:
        print('\nY is at 7, we are almost there!')
        #break <- add this here if you want it to stop at 7
    elif y==10:
        print('DONE!')
    else:
        print('\n...continuing')
        continue

# DO NOT REMOVE

print("**************************** \n End of script \n ****************************")