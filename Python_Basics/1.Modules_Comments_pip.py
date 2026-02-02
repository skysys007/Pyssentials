# Module - a module is a code written by somebody 
# else which can be imported and used in our programs\

# And ofcourse the starter - "Hello World"
print("Hello World")
# pip - pip installs packages
# pip is the package manager for python, which can be used to install a  
# module in your system


#  comments are used to write something which the programmer doesnt want 
# to execute, like documentaion , author name, date, etc..

# Single line comments

"""Multi 
Line 
Comments"""

# installing a module named numpy and performing an operation of my choice
# pip install numpy
import numpy as np
a = [1, 2, 3, 4, 5, 6]
print(np.max(a)) # np.max returns the maximum number from a list

# importing os and listing all the files in the directory
import os
print(os.listdir())

