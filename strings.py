#Strings in python are surrounded by either single or double quotation marks.

name ='Theo'
age = 37

#Concatenate

print('Hello my name is ' + name + 'I am ' + str(age))

# String formatting

#Arguments by position

print('My name is {name} and I am {age}'.format(name=name, age=age))

#F-Strings (3.6+)

 #print(f'Hello my name is{name} and Iam {age}')

#String methods

s = 'hello world'

#Capitalize string

print(s.capitalize())

# Make all Uppercase

print(s.upper())

# Make all lower

print(s.lower())

# Swap Case

print(s.swapcase())

# Get length

print(len(s))

# Replace 

print(s.replace('worl', 'DREK'))

#Find position

print(s.find('h'))


#Split 

print(s.split(' '))


# Join 

print(s.join(' '))