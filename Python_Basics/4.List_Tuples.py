# List - a list is a container in python 
# to store a set of values of sny datatype

list1 = [0, 7, "gagan"]
# a list can be accessed using an index just like a string.

l1 = [1, 111, 23, 54, 77, 2, 0, 56]
print("Original List: ", l1)

# List Methods
# .sort() - updates the list after sortin it
l1.sort()
print("Sorted List: ", l1)
# .reverse() - updates the list after reversing it
l1.reverse()
# .append(element) - adds an element to the last index and updates it
l1.append(-1)
print("Appended List: ", l1)
# .insert(index, element) - adds an element to the given index and updates it
l1.insert(2, 66)
print("Inserted a 2 List: ", l1)
# .pop(index) = removes the element from the given index and updates it
l1.pop(2)
print("Popped at 2 List: ", l1 )
#.remove(element) - removes the element from the list
l1.remove(-1)
print("Removed -1 List: ", l1)

# Tuples - tuples are immutable data type in python
a = () # empty tuple
print(a)
a = (1, ) # tuple with one element needs a comma
print(a)
a = (1, 2, 3) # tuple with multiple elements 
print(a)

a = (1, 7, 2, 2)
# Tuple Methods

# .count(ele) returns the number of times the element occurs in the tuple
print(a.count(2)) 
# .index(ele) returns the first index of the occurence of element in the tuple
print(a.count(2)) 

# user input tuple insertion

fruits = []
for i in range(0, 7):
    fruits.append(input(f"Enter fruit {i+1}: "))

print(fruits)

#Tuple immutability check
# fruits = str(l1) - tuple type cannot be changed as they are immutable

Student_m = []
for i in range(0, 6):
    Student_m.append(int(input(f"Enter marks for Student {i+1}: ")))

print(Student_m)

# List sum
sum = 0
li = [1, 2, 3, 4]
for i in range(0, 4):
    sum += li[i]

print(sum)

tup = (7, 0, 8, 0, 0, 9)
print(tup.count(0))


