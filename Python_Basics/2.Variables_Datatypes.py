# A variable is a name given to a memory location and is used to store data
a = 8 # integer
b = 9.6 # float
stri = "string" # string
boo = True # 

# Operators 
# Arithmetic Operator - +, -, *, /
# Assignment Operator - =, +=, -=
# Comparison Operator - ==, !=, >, >=, <, <=
# Logical Operators: and, or and not

# Type() function and Typecasting
a = 31
print(type(a))#<class 'int'>
b = "31"
print(type(b))#<class 'str'>

c = str(31)
print(type(c))#<class 'str'>

# input() function - allows users to take input from the keyboard as a string
A = input("Enter Name: ")
print(A)

# Adding 2 numbers
x = 10
y = 20
z = x+y
print(z)

# Program to find the remainder
num = 88
z = 5
print(num%z)

# type casting while taking input 
x = int(input("Enter a num: "))
print(type(x))

# finding greater
a = 30
b = 84
greater = a if a>b else b
print(greater)

# finding average
num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
avg = (num1+num2)/2
print(avg)

# finding square
x = int(input("Enter a number to square: "))
x = x**2
print("Squared x: ", x)
