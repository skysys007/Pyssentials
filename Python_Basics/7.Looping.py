# Loops helps us to iterate executing a block of code until a certain condition is met
# while loop - keeps executing until a certain condition is met
i = 1
while(i<=50):
    print(i)
    i = i+1
listt = [1, 2, "hi", "hello", "while", "do"]
i = 0
while(i!=len(listt)):
    print(listt[i])
    i=i+1

#  A for loop is used to iterate through a sequence like list,
#  tuple, or string [iterables]
# range(start, end, step_size) function is used to generate a sequence of numbers in the specified range
for i in range(0, 9, 2):
    print(i)

# Additional else 
# an else is used with a for loop if the code is to be executed when the loop exhausts
l = [1, 7, 8]
for item in l:
    print(item)
else:
    print("Done")

# break - break is used to terminate the current loop and come out of the loop
for i in range(0, 70):
    print(i)
    if i == 3:
        break
# similiarly continue is used to skip the current iteration's code after the statement
for i in range(0, 60):
    print("printing")
    if i == 3:
        continue
    print(i)

# pass - this statement is used to instruct to do nothing
l = [1, 7, 8]
for item in l:
    pass # withoit pass it will throw an error

# MULT TABLE
for i in range(1, 11):
    print(5*i)

# Greet S initials
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if(name[0] == "S"):
        print("Hi there", name)

# Mult using while
i = 0
while i<=10:
    print(i*5)
    i = i+1

# Prime
num = 12
if num <= 1:
    print("num is not Prime")
else:
    i = 2
    Prime = True
    while i < num:
        if num % i == 0:
            Prime = False
            break
        i += 1
    if Prime:
        print("num is Prime")
    else:
        print("num is not Prime")

# Sum of n Natural Numbers
n = 8
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# Factorial
num = 5
fact = 1
for i in range(1, num+1):
    fact*=num
    num -= 1
print(fact)
# *
# ***
# *****
for i in range(0, 3):
    print("*"*(2*i+1))
#   *
#  ***
# *****
n = 3
j = n-1 
for i in range(0, 3):
    print(" "*(j), "*"*(2*i + 1), " "*(j))
    j-=1
n=3

# MULT Reversed
n = 5
for i in range(10, 0, -1):
    print(i*n)
