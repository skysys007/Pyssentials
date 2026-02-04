# The Random Access Memory is volatile and loses all of its contents once the program terminates

# A file is data stored in storage devices
# A python program can talk to the file by reading
# content from it and writing content to it.

# There are two types of files: 
# 1. Text files - .txt, .c
# 1. Binary files - .jpg, .dat

# Opening a File in Python
f = open("file.txt", "r") # opens the file in read mode
# Read Contents
text = f.read()
print(text)
f.close()

# you can also read the file using readline() function which is used to read one line at a time from the file
f = open("file.txt", "r")
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
f.close()

# MODES FOR OPENING A FILE
# r     - open for read
# w     - open for writing
# a     - open for appending
# +     - open for updating
# 'rb'  - open for reading in binary mode
# 'rt'  - open for reading in text mode

# Write files into Python
f = open("file.txt", "w")
# the write function overwrites the existing content from the file with new text 
f.write("This is nice")
f.close()

# opening with 'with' statement
with open("file.txt", "r") as f:
    text = f.read()
# with auto-closes the file
print(text)

# find 'twinkle'
with open("poems.txt", "r") as p:
    poem = p.read()
res = poem.find("twinkle")
if(res>0):
    print("Twinkle found at pos: ", res)
else:
    print("Twinkle not found")

# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi-

# score increases whenever the game() function breaks the Hi-score.
hi_score = 0
def game():
    global hi_score
    increase = int(input("Enter 1 to increase the hi-score"))
    if(increase>0):
        hi_score+=1
        with open("Hi-score.txt", "w") as score:
            score.write(f"Hi-Score: {hi_score}")
game()

# Donkey finder and replace
with open("Donkey.txt", "r") as f:
    text = f.read()
    text = text.replace("donkey", "######")
    text = text.replace("monkey", "######")
    text = text.replace("hell", "######")
with open("Donkey.txt", "w") as f:
    f.write(text)

# MULT TABLE FILE CREATION
def mult(n):
    for i in range(0, 11):
        with open(f"{n}.txt", "a") as m:
            m.write(f"{n} X {i} = {n*i}\n")
        
for i in range(2, 21):
    mult(i)

# mine Python in log file
with open("log.txt", "r") as p:
    for i in range(0, 6):
        text = p.readline()
        found = text.find("Python")
        if(found>=0):
            print(f"Python found at line {i+1}")

# make copy of a this.txt file
with open("this.txt", "r") as c:
    text = c.read()
with open("copy.txt", "w") as c:
    c.write(text)

# check duplicate file
with open("copy.txt", "r") as c:
    copy = c.read()
if(copy == text):
    print("Both file contents are same")

# wipe file content
with open("this.txt", "w") as f:
    f.write("")

# rename file
import os
os.rename("this.txt", "renamed.txt")