# A list is a collection which is ordered and changeable. Allows duplicate members.

#Note: A List in javascript is called Array.

# Create a list

numbers = [1,2,3,4]


fruits=['apples', 'oranges', 'grapes','banana']


#Use a constructor

#numbers2= list((1,2,4,5))

# Get  an index value

#print(fruits[0])

# Get length

print(len(fruits))

#Append to the list

fruits.append('mango')

print(fruits)

#Remove from list 

fruits.remove('mango')

print(fruits)


#Insert into position


fruits.insert(2, 'mango')

print(fruits)

# Remove by pop method

fruits.pop(2)

#Reverse a list

fruits.reverse()

#Sort list

fruits.sort()

# Sort list

fruits.sort(reverse=True)

# Change a value

fruits[2]='pineple'

print(fruits)
#print(numbers, numbers2) 