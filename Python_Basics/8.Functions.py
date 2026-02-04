# Function - A function is a group of statements used to perform a specific task
# A function can be reused by the programmer using the function call
def funct1():
    #Function definition
    print("This function prints")
# now this function can be called any number of times in anywhere in the programmer
funct1() # function call

# program to greet a user (as arguments) with “Good day” 
def greet(user):
    print("Hello,", user)
greet("gagan")
# arguments in a function can be used in the function's definition

# There are two types of functions:
# 1. Built in Functions - len(), print(), range()
# 2. User Defined Functions 

# A function can also return a value
def greet(user):
    return (f"Hello, {user}")
greeting = greet("gagan")
print(greeting)

# Default Parameters
# these parameters are used by default when no parameters in the function call is passed
def uni_id(id = "001"):
    return id
id = uni_id()
print(id)

# Recursion is a function which calls itself
# example: factorial of n = n * fact(n-1)
i = 10
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

# program to find greatest of three numbers.
def got(n1, n2, n3):
    if(n1>=n2 and n1>=n3):
        return n1
    elif(n2 >= n1 and n2 >= n3):
        return n2
    else:
        return n3
    
print(got (3, 5, 3))

# Celsius to Farhenheit
cels = 20
def convert(cels):
    return ((cels*(9/5))+32)
print(convert(cels))

# How do you prevent a python print() function to print a new line at the end.
# using the end parameter

# Star Pattern
def printstar(n):
    for i in range(n, 0, -1):
        print("*" * i)
printstar(3)

# Inches to cm
def toCm(inches):
    print(2.54*inches)
toCm(3)

# Remove and Stri[]
listi = ["     hello     ", " bhai   ", "okkkk  "]
def r_str(list):
    removed  = list[0].strip()
    listi.pop(0)
    return removed

removed = r_str(listi)
print(listi)
print(removed)

# sum of n nums
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
print(sum(3))    

# Function to print mult table
def mult_table(n):
    for i in range(0, 11):
        print(f"{n}*{i} =", n*i)

mult_table(7)