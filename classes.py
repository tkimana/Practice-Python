# A class is like a blueprint for creating objects. An object has properties and methods (funtions) assiciated with it.
#Almost everything in Python is an object.


# Note: A class is a collection of objects.

# Create an Object

class User:

    # Constractor
    def __init__(self, name, email, address, age):
        self.name= name
        self.email= email
        self.address= address
        self.age=age
    
    def greeting(self):
        return f'My name is {self.name} and {self.email} is my email and Im {self.age}'
    def has_birthday(self):
        self.age+=1
# Initialize user object 
brad = User('James Theo', 'theo@gmail.com', '433 bellaire', 35)

brad.has_birthday()
print(brad.greeting())

# Created another class
class Music:

    def __init__(self, genre, dateprod, singer, title, description):
        self.genre=genre
        self.dateprod=dateprod
        self.singer=singer
        self.title= title
        self.description=description

    def profile(self):
        return f'Genre: {self.genre}, DateProd: {self.dateprod}, Singer: {self.singer},Title: {self.title}, Description: {self.description}'



 # Create customer class


class Customer(User):

    def __init__(self, name, email, address, age):
        self.name= name
        self.email= email
        self.address= address
        self.age=age
        self.balance= 0

    def set_balance(self, balance):
        self.balance= balance

    def greeting(self):
        return f'My name is {self.name} and {self.email} is my email and Im {self.age} my balance is {self.balance}'

# Iniitialize a Customer object

Music1= Music('Country Music', '1998', 'Davis J', 'Take it from me', 'This is Jordan Davis Song produced in Nashville')
greg= Customer('greg', 'greg@gmail.com', ' 124 gessner', 233)
print(Music1.profile())
greg.set_balance(320)
print(greg.greeting())





    






