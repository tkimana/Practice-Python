# A class is like a blueprint for creating objects. An object has properties and methods (funtions) assiciated with it.
#Almost everything in Python is an object.


# Note: A class is a collection of objects.

# Create an Object

class User:

    # Constractor
    def __init__(self, name, email, address):
        self.name= name
        self.email= email
        self.address= address
    
    def greeting(self):
        return f'My name is {self.name} and {self.email} is my email'
# Initialize user object 
brad = User('James Theo', 'theo@gmail.com', '433 bellaire')

#print(brad.greeting())

class Music:

    def __init__(self, genre, dateprod, singer, title, description):
        self.genre=genre
        self.dateprod=dateprod
        self.singer=singer
        self.title= title
        self.description=description

    def profile(self):
        return f'Genre: {self.genre}, DateProd: {self.dateprod}, Singer: {self.singer},Title: {self.title}, Description: {self.description}'


Music1= Music('Country Music', '1998', 'Davis J', 'Take it from me', 'This is Jordan Davis Song produced in Nashville')
print(Music1.profile())
 # Create a Method for this class.

    






