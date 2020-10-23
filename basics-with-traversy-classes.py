#A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost everything in Python is an object.

#Create a class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    #methods
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old.'
    
    def hasBirthday(self):
        self.age += 1

#initialize user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)

print(brad.name)
print(brad.email)
print(brad.age)

brad.hasBirthday()
print(brad.greeting())

#Extend Class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age   
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old. My balance is {self.balance}.'

janet = Customer('Janet Johnson', 'janet@gmail.com', 25)
janet.setBalance(500)
print(janet.greeting())