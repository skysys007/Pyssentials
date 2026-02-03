# Conditional Statements are used to execute a block of code based on the 
# condition provided
# if else
# if the condition is true the code block associated with the if statement 
# will be executed
# else the else block will be executed
# age = int(input("Enter your age: "))
# if(age>=18):
#     print("yes")

# RELATIONAL OPERATORS - used to evaluate conditions
# == - equals
# >= - greater than equals
# <= - less than equals
# < - less than 
# > - greater than 

# LOGICAL OPERATORS
# and - returns true if both expressions are true
# or - returns true if one of the expressions is true
# inverts the boolean value

# elif clauses are used to chain multiple conditions in an if else ladder

# program to find the greatest of four numbers
# nums = []
# for i in range(0, 4):
#     nums.append(int(input(f"Enter number {i+1}:")))
# greatest = nums[0] 
# for i in nums:
#     if(i>=greatest):
#         greatest = i

# print("The greatest value is: ", greatest)

# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

s_marks = []
for i in range(0, 3):
    s_marks.append(int(input(f"Enter your Marks for Subject {i+1}: ")))

passed = False
sum = 0
for i in s_marks:
    sum += i
    if(i>=33):
        passed = True
if((sum/3)<40):
    passed = False

if(passed):
    print("PASSED")
else:
    print("FAILED")

# SPAM DETECTOR
comment = "Make a lot of Money"
spam_list = ["Make a lot of Money", "Buy now", "subscribe this", "click this"]
spam = False
for i in spam_list:
    if(comment == i):
        spam = True
if spam:
    print("Comment was Spam")
else:
    print("Comment is not a spam")

# Character length 
username = "username"
if(len(username)>10):
    print("Username contains more than 10 characters")
else:
    print("Username does not contain more than 10 chars")

# String Searching in a list
name = "nm"
present = False
name_list = ["xyz", "gagan", "abc"]
for stringg in name_list:
    if stringg == name:
        present = True
if present:
    print("Name is present")
else:
    print("Name is not present")

# GRADE CAlCULATION
marks = 90
if marks>=90:
    print("GRADE S")
elif marks>=80 and marks<90:
    print("GRADE A")
elif marks>=70 and marks<80:
    print("GRADE B")
elif marks>=60 and marks<70:
    print("GRADE C")
elif marks>=50 and marks<60:
    print("GRADE D")
elif marks<50:
    print("GRADE F")
else:
    print("Invalid Marks")

post = "This post is about skysys"
if(post.find('skysys')>0):
    print("This post talks about skysys")
else:
    print("This post doesn't talk about skysys")