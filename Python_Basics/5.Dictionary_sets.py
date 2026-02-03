# Dictionary - a dictionary is a collection of key value pairs
a = {
    "key":"value", 
    "name":"gagan",
    "num": 6,
    "list": [1, 6, 0, 0, 6] 
}
print(a["key"])
print(a["num"])
# Properties of a Dictionary 
# 1. It is mutable
# 2. It is unordered
# 3. It is indexed with keys
# 2. It cannot contain duplicate keys

# Dictionary Methods
# .items() - returns a list of key-value tuples
print(a.items())                
# .keys() - returns a tuple containing key value pairs
print(a.keys())                                       
# .update({"key":"value"}) - updates dictionary with supplied key value pairs
a.update({"loc":192})
print(a)
a.update({"name":"skysys"})
print(a)
# .get("key") - returns the value of the key provided
print(a.get("name"))

# Sets - A set is a collection of non-repetetive unique elements
# Properties
# 1.Sets are unordered
# 2.Sets are unindexed
# 3.There is no way to change items in sets
# 4.Sets cannot contain duplicate values

# OPERATIONS ON SETS
s = {1, 2, 3, 4}
# len(set) - returns the length of the set
print(len(s))
# s.remove(item) - removes the item from the set and updates it
s.remove(4)
print(s)
# s.(pop)
print(s.pop())
print(s)
# s.union - returns a new set from all items from both sets
uni = s.union({1, 5, 3})
print(uni)
# s.intersection - returns a new set from the common element from both set
inter = uni.intersection({4, 5, 7})
print(inter)
# s.clear() - empties the set
s.clear()
print(s)
#s.add(item) - adds an item to the set
s.add(10)
print(s)

# Hindi to English Dictionary
dictionary = {
    "namaste":"hello", 
    "alvida":"bye",
    "Suprabhaat":"Good Morning"
}
# word = input(f"What do you want to translate to English: {dictionary.keys()}: ")
# print(dictionary.get(word))

# Input 8 numbers in set
s = set()
# for i in range(0,8):
#     x = input(f"Enter number {i+1}: ")
#     s = s.union({x})
# print(s)

# Can we have 18 and '18' in a set
s = {18, '18'}
print(s)

s = set()
s.add(20)
s.add(20.0)
s.add('20')
# What will be the length of the set
print(len(s))

# Type of s
s = {} # dictionary
print(type(s))

# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

dicti = {}
for i in range(0, 2):
    key = input("Enter your Name: ")
    value = input("Favourite Language: ")
    dicti.update({key:value})
print(dicti)
# If the names of 2 friends are same; what will happen to the program in problem 
# the last one's value in the dictionary having the same key will be overwritten
# If languages of two friends are same; what will happen to the program 
# the values will get added with their pairs until the keys are unique  

s = {8, 7, 12, "Harry", [1, 2]}
# all elements of the set must be immutable/hashable
# list is not hashable


