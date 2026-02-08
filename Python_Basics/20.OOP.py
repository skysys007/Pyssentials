# Object Oriented Programming is a programming paradigm in which a larger problem is broken down into simpler problems.
# It focuses on reusability of code(DRY - don't repeat your code)
# Class - a class is a blueprint for creating an object
# when class is defined, a template is defined 
class Student:
    # Methods and Variables
    course = "BCA"
    # self parameter - refers to the instance of the class, it is auto-passed while calling a function from an Object
    def getSalary(self):
        print("Salary is not there")

    # static method - a function that does not use the self parameter
    @staticmethod
    def greet():
        print("Hello User")

    # __init__ method - runs as soon as the object is created
    # aka Constructor 
    def __init__(self, name):
        self.name = name

# Object - an object is an instantiation of a class, memory is allocated only after class instantiation
# Object of the given class can invoke methods and props of the class without revealing the implementation details (encapsulation and Abstraction)

# Creating an Object 
skysys = Student("gagan")
print(skysys.course)

# Changing the Attribute of the class
s2 =  Student("s2")
Student.course = "NIL"
print(s2.course)

# Changing the instance Attributes
skysys.course = "python"
print(skysys.course)

# Function call
skysys.getSalary()
# or 
Student.getSalary(skysys)

# Calling static methods
Student.greet()
skysys.greet()
print(skysys.name)

# Creating details of Microsoft Programmers
class Programmer:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company

    def display(self):
        print(f"Name: {self.name} ")
        print(f"Name: {self.age}")
        print(f"Name: {self.company}")

whoami = Programmer("IDK", 20, "Microsoft")
whoami.display()

# Calculator 
class Calculator:
    def __init__(self, n):
        self.n = n
        print(f"NUMBER: {self.n}")
    @staticmethod
    def greet():
        print("HELLO FELLOW")
    def sq(self):
        sq = (self.n)**2
        print(f"SQUARE: {sq}")
    def cube(self):
        cube = (self.n)**3
        print(f"CUBE: {cube}")
    def sqRoot(self):
        sq_root = (self.n)**(1/2)
        print(f"SQUARE ROOT: {sq_root}")

n1 = Calculator(9)
n1.greet()
n1.sq()
n1.sqRoot()
n1.cube()

# Changing Class Attribute
class x:
    a = 0

obj = x()
obj.a = 123
print(obj.a)
print(x.a)

# Class Train
class Train:
    seats = 10
    def __init__(self):
        self.seats = 0
        self.fare = 0
    def bookTicket(self):
        if(Train.seats>0):
            print("Seat booked Successfully")
            Train.seats -=1
            self.seats +=1
            self.fare+=500;
        else:
            print("Seats are packed")

    def getStatus(self):
        print("Number of Seats left: ", Train.seats)
        print("Number of seats booked by you: ", self.seats)
        print("Total Fare Amount: ", self.fare)
        print("THANK YOU FOR TRAVELLING WITH IRCTC")

c1 = Train()
c1.bookTicket()
c1.bookTicket()
c1.bookTicket()
c1.getStatus()
c2 = Train()
c2.bookTicket()
c2.bookTicket()
c2.bookTicket()
c2.bookTicket()
c2.bookTicket()
c2.getStatus()

# Changing the self parameter
class hello:
    def __init__(mint, name):
        mint.name = name
    
h = hello("gagan")
print(h.name)
# self is just a convention