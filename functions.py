print("**************************** \n The script loaded fine. Please note this is working with Python 3. \n ****************************")

'''
FUNCTIONS
        
'''

def my_addition_func (arg1,arg2):
    """
    Here is my docstring!
    """
    print(arg1 + arg2)

my_addition_func(1,2)

def greeting(name):
    print ("Hello, "+ name)

greeting('Jonathon')

def add_num(num1,num2):
    return num1+num2

x = add_num(4,20)
print(x)

def is_prime(num):
    """
    This function is inteded to check if a number is a prime number or not
    INPUT: a number
    OUTPUT: a print statement whether or not the number is prime
    """
    for n in range(2,num):
        if num % n == 0:
            print('This number is unfortunately not prime')
            break
        else:
            print('The number is prime! :)')

is_prime(12)
is_prime(10)

# DO NOT REMOVE

print("**************************** \n End of script \n ****************************")