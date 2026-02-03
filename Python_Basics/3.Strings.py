# String is a datatype which is a sequence of 
# characters enclosed in ""

# three way to write strings
a = 'string' # single quoted
a = "string" # double quoted
a = '''string''' # triple quoted

name = "gagan"
# String Slicing
# getting a part of the string
# Syntax : sl[start:end]
sl = name[0:3]
print(sl)
# negative indices can also be used 
#        0  1  2  3  4 
# array [1, 2, 3, 4, 5]
#       -5, -4 -3 -2 -1

# Slicing with skip values
word =  'marvellous'
print(word[0:9:3])
print(word[:10]) # [0:10] 
# last index is not included

# String Functions
str = 'gagan'
#len(str)
print(len(str))

# String.endswith("substr"): if string ends with the
# substr at the last it returns true
print(str.endswith("gan"))

# String.count("x"):counts the total number of 
# occurences of the substring in the string
print(str.count("an"))

# String.capitalize(): capitalizes the first char 
# in the string and returns it
caps = str.capitalize()
print(caps)

# String.find(): this function finds a subtring and returns the index of the first occurence of the substring
print(str.find("an"))

# String.replace(old_str, new_string): replaces 
# the old substr with the new substr and returns
# the replaced string
replaced = str.replace("ga", "o")
print(replaced)
# Escape sequence characters 
# \n - new line
# \t - tab
# \` - single quote
# \\ = backslash

# user input name and greet
name = input("Enter your Name: ")
print(name, "Hello")

# replace name and date
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
replaced = letter.replace("<|Name|>", "Gagan", )
replaced = replaced.replace("<|Date|>", "2/02/26")
print(replaced)

# replaced double space
str = "hello  world"
print(str.find("  "))
rep_str = str.replace("  ", " ")
print(rep_str)

# formatting letters
letter = "Dear Harry, this python course is nice. Thanks!"
letter = letter.replace(", t", ",\nT")
letter = letter.replace(". ", ".\n")

print(letter)

